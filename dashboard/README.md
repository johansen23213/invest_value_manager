# ValueHunter Dashboard v1

Streamlit-based dashboard for ValueHunter daily fund operation and external sharing.

## Pages

- **🏠 Glance** — morning operator view: triggered SOs, earnings 7d, macro, top actions today.
- **📊 Portfolio** — active positions, allocation charts, P&L summary.
- **🎯 Pipeline** — quality universe with pipeline funnel + multi-fund conviction.
- **🇪🇸 Spanish Funds** — holdings from 5 Spanish value funds with multi-fund hero section.

## Running locally

```bash
cd invest_value_manager
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
# open http://localhost:8501
```

## Share mode

Toggle "Share mode" in the sidebar, or append `?share=1` to the URL, to anonymize
absolute € values. Percentages and structural info remain visible.

## Deployed URL

Live instance (requires whitelisted Google account): see `DEPLOY.md` for setup and
the current URL (updated at deploy time).

## Data freshness

- Standing orders: 5 min cache.
- Prices (yfinance): 15 min cache.
- Universe, portfolio, spanish funds: 15 min cache.
- Macro: 1 h cache.
- Derived actions + multi-fund signals: 30-60 min cache.

Hit "🔄 Refresh data" in the sidebar to invalidate all caches.

## Data sync (Local → Remote)

The deployed dashboard reads repo files from GitHub. Local state changes
(new theses, portfolio updates, SOs) only reach the dashboard after
`git commit` + `git push` from the local workstation.

## Architecture

- `dashboard/app.py` — entry point + sidebar setup
- `dashboard/sidebar.py` — share_mode, glossary, refresh button
- `dashboard/components.py` — COLOR contract + money/pct formatters
- `dashboard/data_loader.py` — cached data access (YAML/JSON + yfinance + macro subprocess)
- `dashboard/pages/` — 4 Streamlit pages (one per sidebar item)

Pages never read filesystem or call yfinance directly — all data access
goes through `data_loader.py` so caching and share_mode propagation are centralized.

## UX validation

Each page was reviewed by the `elena-dashboard-ux` skill before merge.
See `.claude/skills/elena-dashboard-ux/SKILL.md` for the validation checklist.

## Known limitations

- Mobile works but is not polished.
- Streamlit Cloud free tier RAM limit (1 GB) may constrain large universes.
- Real-time is not a goal — caches mean up to 60 min staleness.
- OAuth whitelist is managed manually in Streamlit Cloud settings.
- Macro data may be "unavailable" on Streamlit Cloud if subprocess restrictions apply.
