#!/usr/bin/env python3
"""
Drift Detector - Framework v4.0
Detecta cambios graduales e inadvertidos en patrones de decisión.

Usage:
  python3 tools/drift_detector.py
  python3 tools/drift_detector.py --verbose
"""
import sys
import os
import yaml
from datetime import datetime, timedelta
from collections import defaultdict

def load_decisions_log():
    """Load decisions log from learning/decisions_log.yaml"""
    path = os.path.join(os.path.dirname(__file__), '..', 'learning', 'decisions_log.yaml')
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: decisions_log.yaml not found")
        return None

def extract_sizing_values(decisions):
    """Extract numeric sizing values from decisions"""
    sizings = []
    for d in decisions:
        sizing = d.get('sizing', '')
        if isinstance(sizing, str) and '%' in sizing:
            try:
                # Handle formats like "4.8%" or "de 2.7% a 5.7%"
                if 'a ' in sizing:
                    # Take the final value
                    val = float(sizing.split('a ')[-1].replace('%', '').strip())
                else:
                    val = float(sizing.replace('%', '').strip())
                sizings.append({
                    'date': d.get('date'),
                    'ticker': d.get('ticker'),
                    'value': val,
                    'tier': d.get('context', {}).get('tier', 'Unknown')
                })
            except:
                pass
    return sizings

def extract_mos_values(decisions):
    """Extract MoS values from decisions"""
    mos_values = []
    for d in decisions:
        context = d.get('context', {})
        mos = context.get('mos', '')
        if isinstance(mos, str) and '%' in mos:
            try:
                val = float(mos.replace('%', '').strip())
                mos_values.append({
                    'date': d.get('date'),
                    'ticker': d.get('ticker'),
                    'value': val,
                    'tier': context.get('tier', 'Unknown')
                })
            except:
                pass
    return mos_values

def analyze_sizing_trend(sizings):
    """Analyze if there's a trend in sizing decisions"""
    if len(sizings) < 3:
        return {
            'status': 'INSUFFICIENT_DATA',
            'message': f"Solo {len(sizings)} decisiones. Necesita ≥3 para detectar tendencia."
        }

    # Calculate average sizing
    values = [s['value'] for s in sizings]
    avg = sum(values) / len(values)

    # Simple trend: compare first half vs second half
    mid = len(values) // 2
    first_half_avg = sum(values[:mid]) / mid if mid > 0 else 0
    second_half_avg = sum(values[mid:]) / len(values[mid:]) if len(values[mid:]) > 0 else 0

    diff = second_half_avg - first_half_avg

    if abs(diff) < 0.5:
        return {
            'status': 'OK',
            'message': f"Sizing estable. Promedio: {avg:.1f}%. Variación: {diff:+.1f}pp",
            'avg': avg,
            'trend': diff
        }
    elif abs(diff) < 1.5:
        return {
            'status': 'REVIEW',
            'message': f"Tendencia leve en sizing. Promedio: {avg:.1f}%. Variación: {diff:+.1f}pp",
            'avg': avg,
            'trend': diff
        }
    else:
        return {
            'status': 'ALERT',
            'message': f"ALERTA: Drift significativo en sizing. Variación: {diff:+.1f}pp",
            'avg': avg,
            'trend': diff
        }

def analyze_mos_threshold(mos_values):
    """Analyze if MoS acceptance threshold is drifting"""
    if len(mos_values) < 3:
        return {
            'status': 'INSUFFICIENT_DATA',
            'message': f"Solo {len(mos_values)} decisiones con MoS. Necesita ≥3."
        }

    # Group by tier
    by_tier = defaultdict(list)
    for m in mos_values:
        by_tier[m['tier']].append(m['value'])

    results = []
    for tier, values in by_tier.items():
        if len(values) >= 2:
            min_mos = min(values)
            avg_mos = sum(values) / len(values)
            results.append({
                'tier': tier,
                'min_accepted': min_mos,
                'avg': avg_mos,
                'count': len(values)
            })

    if not results:
        return {
            'status': 'INSUFFICIENT_DATA',
            'message': "No hay suficientes datos por tier."
        }

    # Return raw data for reasoning - no hardcoded thresholds
    return {
        'status': 'DATA',
        'message': "MoS por tier (datos crudos para razonamiento).",
        'details': results
    }

def analyze_conviction_distribution(decisions):
    """Analyze distribution of conviction levels"""
    convictions = defaultdict(int)
    for d in decisions:
        context = d.get('context', {})
        conv = context.get('conviction', 'Unknown')
        if conv:
            convictions[conv.lower()] += 1

    total = sum(convictions.values())
    if total < 3:
        return {
            'status': 'INSUFFICIENT_DATA',
            'message': f"Solo {total} decisiones con convicción documentada."
        }

    high_pct = convictions.get('alta', 0) / total * 100
    medium_pct = convictions.get('media', 0) / total * 100
    low_pct = convictions.get('baja', 0) / total * 100

    if high_pct > 85:
        return {
            'status': 'REVIEW',
            'message': f"REVISAR: {high_pct:.0f}% de decisiones son 'alta convicción'. Posible inflación.",
            'distribution': dict(convictions)
        }

    return {
        'status': 'OK',
        'message': f"Distribución: Alta {high_pct:.0f}%, Media {medium_pct:.0f}%, Baja {low_pct:.0f}%",
        'distribution': dict(convictions)
    }

def print_report(log, verbose=False):
    """Print drift detection report"""
    print("=" * 70)
    print("DRIFT DETECTION REPORT - Framework v4.0")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    sizing_decisions = log.get('sizing_decisions', [])
    trim_decisions = log.get('trim_decisions', [])
    hold_decisions = log.get('hold_decisions', [])
    all_decisions = sizing_decisions + trim_decisions + hold_decisions

    print(f"\nDecisiones analizadas: {len(all_decisions)}")

    # Metric 1: Sizing Trend
    print(f"\n{'─' * 50}")
    print("MÉTRICA 1: SIZING TREND")
    print(f"{'─' * 50}")

    sizings = extract_sizing_values(sizing_decisions)
    sizing_result = analyze_sizing_trend(sizings)

    status_symbol = {'OK': '✓', 'REVIEW': '⚠', 'ALERT': '✗', 'INSUFFICIENT_DATA': '?'}
    print(f"  [{status_symbol.get(sizing_result['status'], '?')}] {sizing_result['status']}")
    print(f"  {sizing_result['message']}")

    if verbose and sizings:
        print("\n  Detalle de sizings:")
        for s in sizings[-5:]:  # Last 5
            print(f"    {s['date']}: {s['ticker']} → {s['value']:.1f}% (Tier {s['tier']})")

    # Metric 2: MoS Threshold
    print(f"\n{'─' * 50}")
    print("MÉTRICA 2: MoS THRESHOLD")
    print(f"{'─' * 50}")

    mos_values = extract_mos_values(sizing_decisions)
    mos_result = analyze_mos_threshold(mos_values)

    print(f"  [{status_symbol.get(mos_result['status'], '?')}] {mos_result['status']}")
    print(f"  {mos_result['message']}")

    if verbose and 'details' in mos_result:
        print("\n  Por tier:")
        for r in mos_result['details']:
            print(f"    Tier {r['tier']}: min={r['min_accepted']:.0f}%, avg={r['avg']:.0f}% (n={r['count']})")

    # Metric 3: Conviction Distribution
    print(f"\n{'─' * 50}")
    print("MÉTRICA 3: CONVICTION DISTRIBUTION")
    print(f"{'─' * 50}")

    conv_result = analyze_conviction_distribution(sizing_decisions)

    print(f"  [{status_symbol.get(conv_result['status'], '?')}] {conv_result['status']}")
    print(f"  {conv_result['message']}")

    # Metric 4: Decision Frequency
    print(f"\n{'─' * 50}")
    print("MÉTRICA 4: DECISION FREQUENCY")
    print(f"{'─' * 50}")

    if all_decisions:
        dates = [d.get('date') for d in all_decisions if d.get('date')]
        if dates:
            try:
                dates_parsed = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
                most_recent = max(dates_parsed)
                days_since = (datetime.now() - most_recent).days
                print(f"  Última decisión registrada: hace {days_since} días")
                if days_since > 14:
                    print(f"  ⚠ REVISAR: Más de 14 días sin documentar decisiones.")
                else:
                    print(f"  ✓ OK: Decisiones documentadas recientemente.")
            except:
                print("  ? No se pudo analizar frecuencia.")
        else:
            print("  ? No hay fechas en decisiones.")
    else:
        print("  ? No hay decisiones documentadas.")

    # Overall Status
    print(f"\n{'=' * 70}")
    print("OVERALL STATUS")
    print(f"{'=' * 70}")

    statuses = [sizing_result['status'], mos_result['status'], conv_result['status']]
    if 'ALERT' in statuses:
        overall = 'ALERT'
        symbol = '✗'
        action = "ACCIÓN REQUERIDA: Revisar decisiones recientes con el humano."
    elif 'REVIEW' in statuses:
        overall = 'REVIEW'
        symbol = '⚠'
        action = "RECOMENDACIÓN: Revisar las métricas marcadas. Documentar si es intencional."
    else:
        overall = 'OK'
        symbol = '✓'
        action = "El sistema parece consistente. Continuar operando normalmente."

    print(f"\n  [{symbol}] {overall}")
    print(f"\n  {action}")

    # Patterns if available
    patterns = log.get('patterns', {})
    if patterns and verbose:
        print(f"\n{'─' * 50}")
        print("PATRONES DOCUMENTADOS (referencia)")
        print(f"{'─' * 50}")
        sizing_patterns = patterns.get('sizing_by_tier', {})
        for tier, data in sizing_patterns.items():
            print(f"  {tier}: {data.get('typical_range', 'N/A')}")

    print()

def main():
    verbose = '--verbose' in sys.argv or '-v' in sys.argv

    log = load_decisions_log()
    if not log:
        print("ERROR: No se pudo cargar decisions_log.yaml")
        sys.exit(1)

    print_report(log, verbose)

if __name__ == '__main__':
    main()
