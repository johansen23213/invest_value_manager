#!/usr/bin/env python3
"""
Dynamic Stock Screener - Programmatic ticker sourcing, zero popularity bias.

Gets index components from Wikipedia/yfinance programmatically instead of
hardcoded lists. Caches results for 7 days. Parallel yfinance fetching.

SUPERSEDES: screener.py and midcap_screener.py

Usage:
  python3 tools/dynamic_screener.py --index stoxx600          # All STOXX 600
  python3 tools/dynamic_screener.py --index sp500 --pe-max 12
  python3 tools/dynamic_screener.py --index ftse350 --yield-min 4
  python3 tools/dynamic_screener.py --index nikkei225
  python3 tools/dynamic_screener.py --index all               # Combine all indices
  python3 tools/dynamic_screener.py --index custom --file data/my_tickers.csv
  python3 tools/dynamic_screener.py --index stoxx600 --undiscovered
  python3 tools/dynamic_screener.py --index sp500 --max-analysts 5 --near-low
  python3 tools/dynamic_screener.py --index stoxx600 --sort analysts --output results.csv
  python3 tools/dynamic_screener.py --index stoxx600 --workers 20  # Faster parallel fetch
  python3 tools/dynamic_screener.py --refresh                  # Force refresh cache

  # Small & Mid Cap indices:
  python3 tools/dynamic_screener.py --index sp600              # S&P SmallCap 600 (US)
  python3 tools/dynamic_screener.py --index sdax               # SDAX (German Small Cap, ~70 companies)
  python3 tools/dynamic_screener.py --index mdax               # MDAX (German Mid Cap, ~50 companies)
  python3 tools/dynamic_screener.py --index cac_mid60          # CAC Mid 60 (French Mid/Small Cap)
  python3 tools/dynamic_screener.py --index cac_next20         # CAC Next 20 (French Mid Cap)
  python3 tools/dynamic_screener.py --index ftse_aim100        # FTSE AIM 100 (UK Small Cap)
  python3 tools/dynamic_screener.py --index us_smallcap        # = S&P 600
  python3 tools/dynamic_screener.py --index europe_smallcap    # SDAX + CAC Mid60 + CAC Next20 + FTSE AIM100
  python3 tools/dynamic_screener.py --index smallcap_all       # All small caps (US + EU)
  python3 tools/dynamic_screener.py --index german_all         # DAX40 + MDAX + SDAX
  python3 tools/dynamic_screener.py --index french_all         # CAC40 + CAC Mid60 + CAC Next20
  python3 tools/dynamic_screener.py --index smallcap_all --undiscovered  # Best for value: low coverage small caps
"""

import sys
import os
import argparse
import json
import csv
import time
from datetime import datetime, timedelta
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import yfinance as yf

# --- Configuration ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
CACHE_DIR = PROJECT_DIR / "data" / "index_cache"
CACHE_MAX_AGE_DAYS = 7

# --- Wikipedia URLs for index components ---
# Each entry: url, parser function name, and table/column hints
INDEX_SOURCES = {
    "sp500": {
        "url": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
        "parser": "sp500",
    },
    "dax40": {
        "url": "https://en.wikipedia.org/wiki/DAX",
        "parser": "generic_ticker_col",
        "table_min_rows": 35,
        "suffix": ".DE",
    },
    "cac40": {
        "url": "https://en.wikipedia.org/wiki/CAC_40",
        "parser": "generic_ticker_col",
        "table_min_rows": 35,
        "suffix": ".PA",
    },
    "ibex35": {
        "url": "https://en.wikipedia.org/wiki/IBEX_35",
        "parser": "generic_ticker_col",
        "table_min_rows": 30,
        "suffix": ".MC",
    },
    "aex25": {
        "url": "https://en.wikipedia.org/wiki/AEX_index",
        "parser": "generic_ticker_col",
        "table_min_rows": 20,
        "suffix": ".AS",
    },
    "ftse100": {
        "url": "https://en.wikipedia.org/wiki/FTSE_100_Index",
        "parser": "ftse",
        "table_min_rows": 0,  # no component table on main page
    },
    "ftse250": {
        "url": "https://en.wikipedia.org/wiki/FTSE_250_Index",
        "parser": "ftse250",
        "table_min_rows": 200,
    },
    "omx_helsinki": {
        "url": "https://en.wikipedia.org/wiki/OMX_Helsinki_25",
        "parser": "generic_ticker_col",
        "table_min_rows": 20,
        "suffix": ".HE",
    },
    "nikkei225": {
        "url": "https://en.wikipedia.org/wiki/Nikkei_225",
        "parser": "nikkei225",
    },
    "mib40": {
        "url": "https://en.wikipedia.org/wiki/FTSE_MIB",
        "parser": "generic_ticker_col",
        "table_min_rows": 30,
        "suffix": ".MI",
    },
    "omx_stockholm": {
        "url": "https://en.wikipedia.org/wiki/OMX_Stockholm_30",
        "parser": "generic_ticker_col",
        "table_min_rows": 25,
        "suffix": ".ST",
    },
    "obx25": {
        "url": "https://en.wikipedia.org/wiki/OBX_Index",
        "parser": "generic_ticker_col",
        "table_min_rows": 20,
        "suffix": ".OL",
    },
    "smi20": {
        "url": "https://en.wikipedia.org/wiki/Swiss_Market_Index",
        "parser": "generic_ticker_col",
        "table_min_rows": 15,
        "suffix": ".SW",
    },
    "bel20": {
        "url": "https://en.wikipedia.org/wiki/BEL_20",
        "parser": "generic_ticker_col",
        "table_min_rows": 15,
        "suffix": ".BR",
    },
    "psi20": {
        "url": "https://en.wikipedia.org/wiki/PSI_20",
        "parser": "generic_ticker_col",
        "table_min_rows": 15,
        "suffix": ".LS",
    },
    "sp400": {
        "url": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
        "parser": "sp500",  # Same format: Symbol column
    },
    "sp600": {
        "url": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
        "parser": "sp500",  # Same format: Symbol column
    },
    "russell1000": {
        "url": "https://en.wikipedia.org/wiki/Russell_1000_Index",
        "parser": "russell1000",
    },
    "sdax": {
        "url": "https://en.wikipedia.org/wiki/SDAX",
        "parser": "sdax",
    },
    "mdax": {
        "url": "https://en.wikipedia.org/wiki/MDAX",
        "parser": "generic_ticker_col",
        "table_min_rows": 40,
        "suffix": ".DE",
    },
    "ftse_aim100": {
        "url": "https://en.wikipedia.org/wiki/FTSE_AIM_100_Index",
        "parser": "generic_ticker_col",
        "table_min_rows": 50,
        "suffix": ".L",
    },
}

# Composite indices (combine multiple)
COMPOSITE_INDICES = {
    "europe_all": ["dax40", "cac40", "ibex35", "aex25", "ftse100", "ftse250",
                   "omx_helsinki", "mib40", "omx_stockholm", "obx25", "smi20",
                   "bel20", "psi20"],
    "europe_all_caps": ["dax40", "cac40", "ibex35", "aex25", "ftse100", "ftse250",
                        "omx_helsinki", "mib40", "omx_stockholm", "obx25", "smi20",
                        "bel20", "psi20", "sdax", "mdax", "cac_mid60", "cac_next20",
                        "ftse_aim100"],
    "stoxx600": ["dax40", "cac40", "ibex35", "aex25", "ftse100", "ftse250",
                 "omx_helsinki", "mib40", "omx_stockholm", "obx25", "smi20",
                 "bel20", "psi20"],  # best approximation
    "ftse350": ["ftse100", "ftse250"],
    "nordic": ["omx_helsinki", "omx_stockholm", "obx25"],
    "us_all": ["sp500", "sp400", "russell1000"],
    "us_all_caps": ["sp500", "sp400", "sp600", "russell1000"],
    "us_smallcap": ["sp600"],
    "us_midcap": ["sp400"],
    "europe_smallcap": ["sdax", "cac_mid60", "cac_next20", "ftse_aim100"],
    "german_all": ["dax40", "mdax", "sdax"],
    "french_all": ["cac40", "cac_mid60", "cac_next20"],
    "smallcap_all": ["sp600", "sdax", "cac_mid60", "cac_next20", "ftse_aim100"],
}

# Minimal hardcoded fallback (last resort only)
FALLBACK_TICKERS = {
    "stoxx600": [
        "SAN.PA", "BNP.PA", "ENGI.PA", "TTE.PA", "AI.PA", "OR.PA",
        "ISP.MI", "UCG.MI", "ENEL.MI", "ENI.MI", "A2A.MI",
        "BBVA.MC", "SAN.MC", "IBE.MC", "TEF.MC", "REP.MC",
        "ALV.DE", "BAS.DE", "SAP.DE", "SIE.DE", "BMW.DE", "BAYN.DE",
        "HSBA.L", "SHEL.L", "BP.L", "GSK.L", "BARC.L", "LLOY.L",
        "INGA.AS", "ASML.AS", "UNA.AS", "PHIA.AS",
        "NOVN.SW", "NESN.SW", "ROG.SW",
        "NOVO-B.CO", "DSV.CO", "MAERSK-B.CO",
        "EQNR.OL", "DNB.OL", "MOWI.OL",
        "SAMPO.HE", "FORTUM.HE", "UPM.HE",
        "VOLV-B.ST", "SEB-A.ST", "SAND.ST",
    ],
    "sp500": [
        "AAPL", "MSFT", "AMZN", "GOOGL", "META", "BRK-B", "JNJ", "PG",
        "JPM", "V", "UNH", "HD", "PFE", "MRK", "ABBV", "CVX", "XOM",
        "BAC", "WFC", "T", "VZ", "MO", "KO", "PEP", "WMT", "COST",
    ],
    "ftse100": [
        "AAF.L", "AAL.L", "ABF.L", "ADM.L", "AHT.L", "ANTO.L", "AUTO.L",
        "AV.L", "AZN.L", "BA.L", "BARC.L", "BATS.L", "BDEV.L", "BKG.L",
        "BNZL.L", "BP.L", "BRBY.L", "BT-A.L", "CCH.L", "CNA.L", "CPG.L",
        "CRDA.L", "CRH.L", "CTEC.L", "DARK.L", "DCC.L", "DGE.L", "EDV.L",
        "ENT.L", "EXPN.L", "EZJ.L", "FLTR.L", "FRES.L", "GLEN.L", "GSK.L",
        "HIK.L", "HLN.L", "HLMA.L", "HSBA.L", "HWDN.L", "IAG.L", "IHG.L",
        "III.L", "IMB.L", "INF.L", "ITRK.L", "ITV.L", "JD.L", "KGF.L",
        "LAND.L", "LGEN.L", "LLOY.L", "LSEG.L", "MKS.L", "MNDI.L", "MNG.L",
        "MRO.L", "NG.L", "NWG.L", "NXT.L", "PHNX.L", "PRU.L", "PSH.L",
        "PSN.L", "REL.L", "RIO.L", "RKT.L", "RMV.L", "RR.L", "RTO.L",
        "SBRY.L", "SDR.L", "SGE.L", "SGRO.L", "SHEL.L", "SKG.L", "SMDS.L",
        "SMIN.L", "SMT.L", "SN.L", "SPX.L", "SSE.L", "STAN.L", "SVT.L",
        "TSCO.L", "TW.L", "ULVR.L", "UTG.L", "UU.L", "VOD.L", "WEIR.L",
        "WPP.L", "WTB.L",
    ],
    "nikkei225": [
        "7203.T", "6758.T", "9432.T", "8306.T", "6861.T", "9984.T",
        "8058.T", "8001.T", "5020.T", "2914.T", "4502.T", "6501.T",
    ],
    "sp600": [
        "CARG", "CWAN", "DOC", "ENSG", "EXPO", "FIVE", "FOXF", "FSS",
        "GOLF", "HALO", "HRMY", "IBOC", "IPAR", "IRTC", "KLIC", "LANC",
        "LGND", "LNTH", "MGEE", "MMSI", "MTRN", "NOVT", "NSIT", "OMCL",
        "PAYO", "PRGS", "QLYS", "RHP", "SIGI", "SPSC", "SXT", "TNET",
        "TRIP", "TTMI", "VCYT", "VRRM", "WDFC", "WTS", "XRAY",
    ],
    "sdax": [
        "SOW.DE", "BYW6.DE", "G1A.DE", "PBB.DE", "WAF.DE", "DIC.DE",
        "EVT.DE", "SZG.DE", "ADJ.DE", "CWC.DE", "STM.DE", "DHER.DE",
        "JUN3.DE", "SGL.DE", "BOSS.DE", "GXI.DE", "BC8.DE", "KWS.DE",
        "TEG.DE", "VBK.DE", "AIXA.DE", "PNE3.DE", "NEM.DE", "BNR.DE",
        "HHFA.DE", "INH.DE", "S92.DE", "HLAG.DE", "FPE3.DE", "AG1.DE",
        "WCH.DE", "SY1.DE", "SRT3.DE", "NDX1.DE", "HBH.DE", "ECV.DE",
        "TPE.DE", "SKB.DE", "VAR1.DE", "PUM.DE", "SBS.DE", "O2D.DE",
        "FNTN.DE", "MBB.DE", "UTDI.DE", "SFQ.DE", "HAB.DE", "JDC.DE",
        "NB2.DE", "NOEJ.DE", "DATA.DE", "FTK.DE", "COP.DE", "ARL.DE",
        "CLIQ.DE", "AMG.DE", "HHFA.DE", "TTK.DE", "SIS.DE", "VOS.DE",
        "DBK.DE", "GLJ.DE", "GBF.DE", "PFV.DE", "ACX.DE", "TIM.DE",
    ],
    "cac_mid60": [
        "AF.PA", "AKE.PA", "ALBI.PA", "ALO.PA", "AMUN.PA", "ARG.PA",
        "ATO.PA", "BIM.PA", "BOL.PA", "COFA.PA", "COVH.PA", "DBV.PA",
        "DEXB.PA", "DIM.PA", "EL.PA", "ELIOR.PA", "ERF.PA", "ETL.PA",
        "FDR.PA", "FGR.PA", "GBT.PA", "GFC.PA", "GLE.PA", "GNFT.PA",
        "GTT.PA", "ILD.PA", "ING.PA", "IPN.PA", "IPSO.PA", "JXR.PA",
        "KER.PA", "LNA.PA", "MERY.PA", "MMT.PA", "MRN.PA", "NEX.PA",
        "NOKIA.PA", "OVH.PA", "PAT.PA", "QDT.PA", "RCO.PA", "RF.PA",
        "RNO.PA", "RUBIS.PA", "RXL.PA", "SBT.PA", "SCR.PA", "SEV.PA",
        "SK.PA", "SLB.PA", "SOI.PA", "SPIE.PA", "SRP.PA", "TFI.PA",
        "TKO.PA", "UBI.PA", "VIRP.PA", "VIV.PA", "VRLA.PA", "WLN.PA",
    ],
    "cac_next20": [
        "AC.PA", "BON.PA", "CAT31.PA", "CDA.PA", "CRAP.PA", "DSY.PA",
        "FDJ.PA", "GDS.PA", "HEXA.PA", "IDL.PA", "IPS.PA", "LR.PA",
        "MC.PA", "OR.PA", "PUB.PA", "SAF.PA", "SGO.PA", "SU.PA",
        "VIE.PA", "VLA.PA",
    ],
    "ftse_aim100": [
        "FEVR.L", "BVXP.L", "JET2.L", "GAW.L", "LOK.L", "FDEV.L",
        "TET.L", "ABDP.L", "RWS.L", "CVS.L", "SDI.L", "NWF.L",
        "BOO.L", "GYM.L", "RBGP.L", "TSTL.L", "KITW.L", "DPH.L",
        "TBCG.L", "IGP.L", "ALFA.L", "PHO.L", "KWS.L", "SBIZ.L",
        "IXI.L", "LIO.L", "JTC.L", "BBH.L", "IHP.L", "YCA.L",
        "SEPL.L", "CML.L", "PHNX.L", "CINE.L", "LUCE.L", "SRC.L",
        "HYNS.L", "RBG.L", "TUNE.L", "WINE.L", "KNOS.L", "LSE.L",
        "VLX.L", "NICK.L", "PRTC.L", "CAML.L", "JLG.L", "MTRO.L",
    ],
}


# ==============================================================================
# Index component fetching
# ==============================================================================

def _cache_path(index_name: str) -> Path:
    return CACHE_DIR / f"{index_name}.json"


def _cache_is_valid(index_name: str) -> bool:
    p = _cache_path(index_name)
    if not p.exists():
        return False
    data = json.loads(p.read_text())
    cached_time = datetime.fromisoformat(data.get("timestamp", "2000-01-01"))
    return (datetime.now() - cached_time) < timedelta(days=CACHE_MAX_AGE_DAYS)


def _save_cache(index_name: str, tickers: list):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    data = {"timestamp": datetime.now().isoformat(), "tickers": tickers}
    _cache_path(index_name).write_text(json.dumps(data, indent=2))
    print(f"  Cached {len(tickers)} tickers for {index_name}", file=sys.stderr)


def _load_cache(index_name: str) -> list:
    p = _cache_path(index_name)
    if p.exists():
        data = json.loads(p.read_text())
        tickers = data.get("tickers", [])
        ts = data.get("timestamp", "unknown")
        print(f"  Loaded {len(tickers)} cached tickers for {index_name} (from {ts})", file=sys.stderr)
        return tickers
    return []


def _fetch_wikipedia_tables(url: str):
    """Fetch all tables from a Wikipedia page using pandas + requests."""
    import pandas as pd
    import requests
    from io import StringIO
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
        r.raise_for_status()
        tables = pd.read_html(StringIO(r.text))
        return tables
    except Exception as e:
        print(f"  Wikipedia fetch failed: {e}", file=sys.stderr)
        return []


def _find_ticker_column(df):
    """Heuristic to find the ticker/symbol column in a DataFrame."""
    candidates = ["ticker", "symbol", "code", "epic", "tidm",
                  "stock symbol", "company symbol"]
    for col in df.columns:
        col_lower = str(col).lower().strip()
        if col_lower in candidates:
            return col
    # Check for columns containing mostly short uppercase strings with dots/dashes (tickers)
    for col in df.columns:
        sample = df[col].dropna().head(20).astype(str)
        if len(sample) > 0:
            avg_len = sample.str.len().mean()
            upper_frac = (sample.str.match(r'^[A-Z0-9.\-]+$')).mean()
            has_dots = sample.str.contains(r'\.').mean()
            # Must look like tickers not years: require dots OR dashes OR letters
            has_letters = sample.str.contains(r'[A-Z]').mean()
            if avg_len < 12 and upper_frac > 0.7 and has_letters > 0.5:
                # Reject columns that are all numeric (likely years)
                all_numeric = sample.str.match(r'^\d+$').mean()
                if all_numeric < 0.5:
                    return col
    return None


def _parse_sp500(tables) -> list:
    """Parse S&P 500 from Wikipedia - first table has 'Symbol' column."""
    for df in tables:
        if "Symbol" in df.columns:
            return _clean_tickers(df["Symbol"].dropna().astype(str).tolist())
        for col in df.columns:
            if str(col).lower() == "symbol":
                return _clean_tickers(df[col].dropna().astype(str).tolist())
    for df in sorted(tables, key=len, reverse=True):
        tc = _find_ticker_column(df)
        if tc and len(df) > 100:
            return _clean_tickers(df[tc].dropna().astype(str).tolist())
    return []


def _parse_generic_ticker_col(tables, min_rows=20, suffix=None) -> list:
    """Generic parser: find table with Ticker column, optionally add suffix."""
    for df in tables:
        tc = _find_ticker_column(df)
        if tc and len(df) >= min_rows:
            raw = df[tc].dropna().astype(str).tolist()
            if suffix:
                raw = [t + suffix if "." not in t else t for t in raw]
            return _clean_tickers(raw)
    return []


def _parse_ftse(tables, **kwargs) -> list:
    """FTSE 100 main page doesn't have component table. Use fallback."""
    # The FTSE 100 Wikipedia page doesn't list components
    # Return empty to trigger fallback to hardcoded FTSE 100 list
    return []


def _parse_ftse250(tables, **kwargs) -> list:
    """FTSE 250 - table with Company/Ticker columns, ~250 rows."""
    for df in tables:
        # Look for Ticker column
        for col in df.columns:
            col_str = str(col).lower()
            if 'ticker' in col_str:
                raw = df[col].dropna().astype(str).tolist()
                raw = [t.strip() + ".L" if "." not in t.strip() else t.strip() for t in raw]
                if len(raw) > 100:
                    return _clean_tickers(raw)
    return []


def _parse_nikkei225(tables, **kwargs) -> list:
    """Parse Nikkei 225 from Wikipedia."""
    for df in tables:
        tc = _find_ticker_column(df)
        if tc and len(df) >= 100:
            raw = df[tc].dropna().astype(str).tolist()
            tickers = []
            for t in raw:
                t = t.strip()
                if t.isdigit():
                    t = t + ".T"
                elif not t.endswith(".T") and "." not in t:
                    t = t + ".T"
                tickers.append(t)
            return _clean_tickers(tickers)
    return []


def _parse_russell1000(tables, **kwargs) -> list:
    """Parse Russell 1000 from Wikipedia - large table with Ticker/Symbol column."""
    for df in tables:
        tc = _find_ticker_column(df)
        if tc and len(df) >= 500:
            return _clean_tickers(df[tc].dropna().astype(str).tolist())
    # Fallback: try any table with >100 rows
    for df in sorted(tables, key=len, reverse=True):
        tc = _find_ticker_column(df)
        if tc and len(df) > 100:
            return _clean_tickers(df[tc].dropna().astype(str).tolist())
    return []


def _parse_sdax(tables, **kwargs) -> list:
    """SDAX Wikipedia page has Name/Industry/Location but no ticker column.
    Falls through to hardcoded fallback which has comprehensive ticker list."""
    # The SDAX Wikipedia page doesn't include ticker symbols
    return []


PARSERS = {
    "sp500": _parse_sp500,
    "russell1000": _parse_russell1000,
    "generic_ticker_col": _parse_generic_ticker_col,
    "ftse": _parse_ftse,
    "ftse250": _parse_ftse250,
    "nikkei225": _parse_nikkei225,
    "sdax": _parse_sdax,
}


def _clean_tickers(tickers: list) -> list:
    """Clean and deduplicate ticker list."""
    cleaned = []
    seen = set()
    for t in tickers:
        t = str(t).strip()
        # Skip junk
        if not t or t == "nan" or len(t) > 20 or " " in t:
            continue
        # Normalize BRK.B style
        t = t.replace(".", "-", 1) if t.count(".") > 1 else t
        if t not in seen:
            seen.add(t)
            cleaned.append(t)
    return cleaned


def get_index_tickers(index_name: str, force_refresh: bool = False,
                      custom_file: str = None) -> list:
    """
    Get tickers for an index. Priority:
    1. Valid cache (< 7 days old)
    2. Wikipedia scrape
    3. Stale cache (any age)
    4. Hardcoded fallback
    """
    if index_name == "custom":
        if not custom_file:
            print("ERROR: --file required with --index custom", file=sys.stderr)
            sys.exit(1)
        return _load_custom_file(custom_file)

    if index_name == "all":
        all_tickers = []
        for idx in INDEX_SOURCES:
            all_tickers.extend(get_index_tickers(idx, force_refresh=force_refresh))
        return list(set(all_tickers))

    # Composite indices (combine multiple sub-indices)
    if index_name in COMPOSITE_INDICES:
        combined = []
        for sub_idx in COMPOSITE_INDICES[index_name]:
            combined.extend(get_index_tickers(sub_idx, force_refresh=force_refresh))
        return list(set(combined))

    # 1. Check cache
    if not force_refresh and _cache_is_valid(index_name):
        return _load_cache(index_name)

    # 2. Try Wikipedia
    source = INDEX_SOURCES.get(index_name)
    if source:
        print(f"  Fetching {index_name} components from Wikipedia...", file=sys.stderr)
        tables = _fetch_wikipedia_tables(source["url"])
        if tables:
            parser = PARSERS.get(source["parser"])
            if parser:
                # Pass extra kwargs from source config (suffix, table_min_rows, etc.)
                kwargs = {k: v for k, v in source.items() if k not in ("url", "parser")}
                if "table_min_rows" in kwargs:
                    kwargs["min_rows"] = kwargs.pop("table_min_rows")
                tickers = parser(tables, **kwargs)
                if len(tickers) > 10:
                    _save_cache(index_name, tickers)
                    return tickers
                else:
                    print(f"  Parser returned only {len(tickers)} tickers, trying fallback", file=sys.stderr)

    # 3. Stale cache
    stale = _load_cache(index_name)
    if stale:
        print(f"  Using stale cache for {index_name}", file=sys.stderr)
        return stale

    # 4. Hardcoded fallback
    fallback = FALLBACK_TICKERS.get(index_name, [])
    if fallback:
        print(f"  Using hardcoded fallback ({len(fallback)} tickers) for {index_name}", file=sys.stderr)
    else:
        print(f"  ERROR: No data available for index '{index_name}'", file=sys.stderr)
    return fallback


def _load_custom_file(filepath: str) -> list:
    """Load tickers from CSV. Expects first column to be ticker symbols."""
    p = Path(filepath)
    if not p.exists():
        # Try relative to project dir
        p = PROJECT_DIR / filepath
    if not p.exists():
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    tickers = []
    with open(p, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                t = row[0].strip()
                if t and not t.lower().startswith("ticker") and not t.lower().startswith("symbol"):
                    tickers.append(t)
    print(f"  Loaded {len(tickers)} tickers from {filepath}", file=sys.stderr)
    return _clean_tickers(tickers)


# ==============================================================================
# FX rates
# ==============================================================================

def get_fx_rates():
    """Get FX rates for EUR conversion. Reports fallback usage."""
    rates = {}
    fallbacks_used = []
    pairs = {"USD": "EURUSD=X", "GBP": "GBPEUR=X"}
    defaults = {"USD": 1.04, "GBP": 1.19}
    for ccy, symbol in pairs.items():
        try:
            rate = yf.Ticker(symbol).info.get("previousClose")
            if rate:
                rates[ccy] = rate
            else:
                rates[ccy] = defaults[ccy]
                fallbacks_used.append(f"{ccy}={defaults[ccy]}")
        except Exception:
            rates[ccy] = defaults[ccy]
            fallbacks_used.append(f"{ccy}={defaults[ccy]}")
    if fallbacks_used:
        print(f"  FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). "
              f"EUR amounts may be inaccurate.", file=sys.stderr)
    return rates


def to_eur(value, currency, rates):
    """Convert value to EUR."""
    if not value:
        return 0
    if currency == "EUR":
        return value
    if currency == "USD":
        return value / rates.get("USD", 1.04)
    if currency in ("GBp", "GBX"):
        return (value / 100) * rates.get("GBP", 1.19)
    if currency == "GBP":
        return value * rates.get("GBP", 1.19)
    if currency in ("SEK", "NOK", "DKK"):
        return value * 0.087
    if currency == "CHF":
        return value * 0.95
    if currency == "JPY":
        return value * 0.0063
    return value  # assume EUR-ish


# ==============================================================================
# Screening
# ==============================================================================

def fetch_stock_data(ticker: str) -> dict:
    """Fetch all data for a single ticker. Returns dict or None."""
    try:
        info = yf.Ticker(ticker).info
        price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
        if not price:
            return None

        pe = info.get("trailingPE")
        if not pe or pe <= 0:
            return None

        # Dividend yield normalization
        dy = info.get("dividendYield", 0)
        if dy and dy > 1:
            dy_pct = dy
        elif dy:
            dy_pct = dy * 100
        else:
            dy_pct = 0

        mcap = info.get("marketCap", 0)
        h52 = info.get("fiftyTwoWeekHigh", 0)
        l52 = info.get("fiftyTwoWeekLow", 0)
        dist_high = ((price - h52) / h52 * 100) if h52 else 0

        fcf = info.get("freeCashflow", 0)
        fcf_yield = (fcf / mcap * 100) if (mcap and fcf) else 0

        de_raw = info.get("debtToEquity", 0)
        debt_equity = de_raw / 100 if de_raw else 0

        return {
            "ticker": ticker,
            "name": (info.get("shortName") or ticker)[:30],
            "price": price,
            "currency": info.get("currency", "?"),
            "mcap": mcap,
            "pe": pe,
            "fwd_pe": info.get("forwardPE"),
            "pb": info.get("priceToBook"),
            "div_yield": dy_pct,
            "fcf_yield": fcf_yield,
            "debt_equity": debt_equity,
            "num_analysts": info.get("numberOfAnalystOpinions", 0) or 0,
            "sector": info.get("sector", "Unknown"),
            "h52": h52,
            "l52": l52,
            "dist_high": dist_high,
        }
    except Exception as e:
        print(f"  SKIP {ticker}: {e}", file=sys.stderr)
        return None


def screen(tickers: list, workers: int = 10, **filters) -> list:
    """
    Screen tickers in parallel. Returns filtered, enriched list of dicts.
    """
    pe_max = filters.get("pe_max", 999)
    pe_min = filters.get("pe_min", 0)
    yield_min = filters.get("yield_min", 0)
    mcap_min = filters.get("mcap_min", 0)  # in billions EUR
    mcap_max = filters.get("mcap_max", 999999)
    near_low_pct = filters.get("near_low_pct", None)  # e.g., -15 means >15% below high
    max_debt_equity = filters.get("max_debt_equity", 999)
    min_fcf_yield = filters.get("min_fcf_yield", 0)
    max_analysts = filters.get("max_analysts", 999999)
    undiscovered = filters.get("undiscovered", False)

    # --undiscovered uses explicit CLI values for max_analysts and mcap_max
    # (defaults: 10 analysts, 15B EUR — overrideable via --max-analysts and --mcap-max)
    undiscovered_analysts = filters.get("undiscovered_analysts", 10)
    undiscovered_mcap = filters.get("undiscovered_mcap", 15)
    if undiscovered:
        max_analysts = min(max_analysts, undiscovered_analysts)
        mcap_max = min(mcap_max, undiscovered_mcap)

    rates = get_fx_rates()
    results = []
    total = len(tickers)
    done = 0
    skipped = 0

    print(f"\nFetching data for {total} tickers ({workers} workers)...", file=sys.stderr)
    t0 = time.time()

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(fetch_stock_data, t): t for t in tickers}
        for future in as_completed(futures):
            done += 1
            if done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  Progress: {done}/{total} ({elapsed:.0f}s)", file=sys.stderr)

            data = future.result()
            if data is None:
                skipped += 1
                continue

            # Convert mcap to EUR billions
            mcap_eur_b = to_eur(data["mcap"], data["currency"], rates) / 1e9
            data["mcap_eur_b"] = mcap_eur_b
            data["price_eur"] = to_eur(data["price"], data["currency"], rates)

            # Apply filters
            if data["pe"] < pe_min or data["pe"] > pe_max:
                continue
            if data["div_yield"] < yield_min:
                continue
            if mcap_eur_b < mcap_min or mcap_eur_b > mcap_max:
                continue
            if near_low_pct is not None and data["dist_high"] > near_low_pct:
                continue
            if data["debt_equity"] > max_debt_equity:
                continue
            if data["fcf_yield"] < min_fcf_yield:
                continue
            if data["num_analysts"] > max_analysts:
                continue

            results.append(data)

    elapsed = time.time() - t0
    print(f"  Done: {done} fetched, {skipped} skipped, {len(results)} passed filters ({elapsed:.0f}s)", file=sys.stderr)
    return results


# ==============================================================================
# Data Validation
# ==============================================================================

def validate_results(results: list) -> dict:
    """
    Flag outlier data points for manual verification.
    Returns dict mapping ticker -> list of flag strings.
    Flags are NEUTRAL observations, not judgments — REITs with 15%+ yield
    or cyclicals with P/E <2 may be legitimate.
    """
    flags = {}  # ticker -> [flag_str, ...]

    for r in results:
        ticker = r["ticker"]
        issues = []

        if r["div_yield"] > 15:
            issues.append(f"Div yield {r['div_yield']:.1f}% — verify source")
        if r["pe"] < 2:
            issues.append(f"P/E {r['pe']:.1f} — verify (one-off earnings?)")
        if r["pe"] > 200:
            issues.append(f"P/E {r['pe']:.1f} — verify (depressed earnings?)")
        if r["fcf_yield"] > 50:
            issues.append(f"FCF yield {r['fcf_yield']:.1f}% — verify (IFRS16? one-off?)")

        if issues:
            flags[ticker] = issues
            r["_flag_yield"] = r["div_yield"] > 15
            r["_flag_pe"] = r["pe"] < 2 or r["pe"] > 200
            r["_flag_fcf"] = r["fcf_yield"] > 50
        else:
            r["_flag_yield"] = False
            r["_flag_pe"] = False
            r["_flag_fcf"] = False

    return flags


# ==============================================================================
# Output
# ==============================================================================

SORT_KEYS = {
    "pe": lambda x: x["pe"],
    "fcf_yield": lambda x: -x["fcf_yield"],
    "div_yield": lambda x: -x["div_yield"],
    "mcap": lambda x: x["mcap_eur_b"],
    "analysts": lambda x: x["num_analysts"],
    "dist_high": lambda x: x["dist_high"],
}


def print_table(results: list, sort_by: str = "pe", warnings: dict = None):
    if not results:
        print("\nNo stocks passed filters.")
        return

    if warnings is None:
        warnings = {}

    key_fn = SORT_KEYS.get(sort_by, SORT_KEYS["pe"])
    results.sort(key=key_fn)

    header = (f"{'Ticker':<14} {'Name':<30} {'Price':>8} {'EUR':>8} "
              f"{'MCap\u20acB':>7} {'P/E':>6} {'FwdPE':>7} {'Yld%':>5} "
              f"{'FCF%':>5} {'D/E':>5} {'%offHi':>7} {'Anlys':>6} {'Sector':<20}")
    print(f"\n{header}")
    print("-" * len(header))

    for r in results:
        fwd_pe = f"{r['fwd_pe']:.1f}" if r["fwd_pe"] else "N/A"
        coverage = f"{r['num_analysts']}"
        if r["num_analysts"] < 5:
            coverage += " *"  # flag low coverage

        # Add flag markers to outlier metrics
        f_pe = "[!]" if r.get("_flag_pe") else ""
        f_yld = "[!]" if r.get("_flag_yield") else ""
        f_fcf = "[!]" if r.get("_flag_fcf") else ""

        pe_str = f"{r['pe']:>5.1f}{f_pe}"
        yld_str = f"{r['div_yield']:>4.1f}{f_yld}"
        fcf_str = f"{r['fcf_yield']:>4.1f}{f_fcf}"

        print(f"{r['ticker']:<14} {r['name']:<30} {r['price']:>8.2f} "
              f"{r['price_eur']:>7.2f}e "
              f"{r['mcap_eur_b']:>7.1f} {pe_str:>6} {fwd_pe:>7} "
              f"{yld_str:>5} {fcf_str:>5} "
              f"{r['debt_equity']:>5.2f} {r['dist_high']:>+6.1f}% "
              f"{coverage:>6} {r['sector']:<20}")

    # Summary
    n = len(results)
    avg_pe = sum(r["pe"] for r in results) / n
    avg_yield = sum(r["div_yield"] for r in results) / n
    avg_fcf = sum(r["fcf_yield"] for r in results) / n
    avg_analysts = sum(r["num_analysts"] for r in results) / n
    low_cov = sum(1 for r in results if r["num_analysts"] < 5)
    med_cov = sum(1 for r in results if r["num_analysts"] < 10)

    print(f"\n{n} stocks passed filters")
    print(f"Averages: P/E={avg_pe:.1f} | Yield={avg_yield:.1f}% | FCF={avg_fcf:.1f}% | Analysts={avg_analysts:.0f}")
    print(f"Low coverage (<5 analysts): {low_cov} ({low_cov/n*100:.0f}%) | Medium (<10): {med_cov} ({med_cov/n*100:.0f}%)")

    if low_cov > 0:
        print(f"\nLOW COVERAGE stocks (potential market inefficiency):")
        for r in sorted([r for r in results if r["num_analysts"] < 5],
                        key=lambda x: x["num_analysts"]):
            print(f"  {r['ticker']:<14} {r['name']:<30} {r['num_analysts']} analysts | "
                  f"P/E={r['pe']:.1f} | Yield={r['div_yield']:.1f}% | MCap={r['mcap_eur_b']:.1f}B")

    # Outlier data flags section
    if warnings:
        print(f"\n{'='*60}")
        print(f"OUTLIER DATA [!]: {len(warnings)} stock(s) — verify before using:")
        print(f"{'='*60}")
        for ticker, issues in sorted(warnings.items()):
            for issue in issues:
                print(f"  [!] {ticker:<14} {issue}")
        print(f"{'='*60}")


def save_csv(results: list, filepath: str):
    if not results:
        print("No results to save.")
        return
    fieldnames = ["ticker", "name", "price", "currency", "price_eur", "mcap_eur_b",
                  "pe", "fwd_pe", "pb", "div_yield", "fcf_yield", "debt_equity",
                  "num_analysts", "sector", "dist_high", "h52", "l52"]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)
    print(f"\nResults saved to {filepath}")


# ==============================================================================
# CLI
# ==============================================================================

def main():
    available_indices = list(INDEX_SOURCES.keys()) + list(COMPOSITE_INDICES.keys()) + ["all", "custom"]
    parser = argparse.ArgumentParser(
        description="Dynamic Stock Screener - programmatic ticker sourcing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available indices: {', '.join(available_indices)}

Examples:
  python3 tools/dynamic_screener.py --index stoxx600
  python3 tools/dynamic_screener.py --index sp500 --pe-max 12 --yield-min 3
  python3 tools/dynamic_screener.py --index stoxx600 --undiscovered
  python3 tools/dynamic_screener.py --index all --near-low 20 --sort dist_high
  python3 tools/dynamic_screener.py --index custom --file data/my_tickers.csv
  python3 tools/dynamic_screener.py --refresh --index stoxx600  # force re-fetch
        """,
    )

    # Index selection
    parser.add_argument("--index", type=str, required=True,
                        help=f"Index to screen: {', '.join(available_indices)}")
    parser.add_argument("--file", type=str, default=None,
                        help="CSV file with tickers (for --index custom)")
    parser.add_argument("--refresh", action="store_true",
                        help="Force refresh cache from Wikipedia")

    # Filters
    parser.add_argument("--pe-max", type=float, default=999, help="Max trailing P/E (default: 999 = no filter)")
    parser.add_argument("--pe-min", type=float, default=0, help="Min trailing P/E (default: 0)")
    parser.add_argument("--yield-min", type=float, default=0, help="Min dividend yield %% (default: 0)")
    parser.add_argument("--mcap-min", type=float, default=0, help="Min market cap EUR billions (default: 0)")
    parser.add_argument("--mcap-max", type=float, default=999999, help="Max market cap EUR billions")
    parser.add_argument("--near-low", type=float, default=None, metavar="PCT",
                        help="Only stocks >PCT%% below 52w high (e.g., 15)")
    parser.add_argument("--max-debt-equity", type=float, default=999, help="Max debt/equity ratio")
    parser.add_argument("--min-fcf-yield", type=float, default=0, help="Min FCF yield %%")
    parser.add_argument("--max-analysts", type=int, default=999999, help="Max analyst coverage")
    parser.add_argument("--undiscovered", action="store_true",
                        help="Filter: low analyst coverage AND small mcap (defaults: <10 analysts, <15B EUR)")
    parser.add_argument("--undiscovered-analysts", type=int, default=10,
                        help="Max analysts for --undiscovered (default: 10)")
    parser.add_argument("--undiscovered-mcap", type=float, default=15,
                        help="Max mcap EUR billions for --undiscovered (default: 15)")

    # Output
    parser.add_argument("--sort", choices=list(SORT_KEYS.keys()), default="pe",
                        help="Sort by (default: pe)")
    parser.add_argument("--output", type=str, help="Save results to CSV")
    parser.add_argument("--workers", type=int, default=10, help="Parallel workers (default: 10)")

    args = parser.parse_args()

    # Get tickers
    print(f"Dynamic Screener - Index: {args.index}", file=sys.stderr)
    tickers = get_index_tickers(args.index, force_refresh=args.refresh,
                                custom_file=args.file)

    if not tickers:
        print("ERROR: No tickers found.", file=sys.stderr)
        sys.exit(1)

    # Build filter description
    filters_desc = []
    if args.pe_max < 998: filters_desc.append(f"P/E<{args.pe_max}")
    if args.yield_min > 0: filters_desc.append(f"Yield>{args.yield_min}%")
    if args.mcap_min > 0: filters_desc.append(f"MCap>{args.mcap_min}B")
    if args.mcap_max < 999999: filters_desc.append(f"MCap<{args.mcap_max}B")
    if args.near_low: filters_desc.append(f">{args.near_low}% off high")
    if args.max_analysts < 999999: filters_desc.append(f"Analysts<={args.max_analysts}")
    if args.undiscovered: filters_desc.append("UNDISCOVERED mode")
    print(f"Filters: {', '.join(filters_desc) if filters_desc else 'none'}", file=sys.stderr)

    near_low_val = -abs(args.near_low) if args.near_low else None

    results = screen(
        tickers,
        workers=args.workers,
        pe_max=args.pe_max,
        pe_min=args.pe_min,
        yield_min=args.yield_min,
        mcap_min=args.mcap_min,
        mcap_max=args.mcap_max,
        near_low_pct=near_low_val,
        max_debt_equity=args.max_debt_equity,
        min_fcf_yield=args.min_fcf_yield,
        max_analysts=args.max_analysts,
        undiscovered=args.undiscovered,
        undiscovered_analysts=args.undiscovered_analysts,
        undiscovered_mcap=args.undiscovered_mcap,
    )

    # Validate data before display
    warnings = validate_results(results)

    print_table(results, sort_by=args.sort, warnings=warnings)

    if args.output:
        save_csv(results, args.output)


if __name__ == "__main__":
    main()
