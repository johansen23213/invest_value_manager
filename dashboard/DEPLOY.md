# ValueHunter Dashboard — Streamlit Cloud Deploy Checklist

Deploy the dashboard to Streamlit Cloud with Google OAuth whitelist.

## Prerequisites

- GitHub account access to `johansen23213/invest_value_manager` (origin remote)
- Google account for Streamlit Cloud login
- Current working branch: `sprint1/foundations`

## Deploy steps

### 1. Log in to Streamlit Cloud
   - Go to https://share.streamlit.io
   - Sign in with Joan's Google account

### 2. Create new app
   - Click "New app"
   - Fill in:
     - **Repository:** `johansen23213/invest_value_manager`
     - **Branch:** `sprint1/foundations`
     - **Main file:** `dashboard/app.py`
   - Click "Advanced settings":
     - **Python version:** 3.12
     - **Requirements file:** should auto-detect `dashboard/requirements.txt`
   - Click "Deploy"

### 3. Wait for initial build
   - First build takes 3-5 minutes
   - Watch the Streamlit Cloud console for import errors or missing dependencies
   - If build fails, check requirements.txt pins and Python version compatibility

### 4. Verify app loads
   - Once deployed, Streamlit assigns a URL like `https://valuehunter-<hash>.streamlit.app`
   - Open URL in browser → should show landing page with sidebar navigation

### 5. Configure OAuth whitelist
   - In Streamlit Cloud dashboard, open app → "Settings" → "Sharing"
   - Select "Only specific people" (restrict access mode)
   - Add Joan's email first
   - Save → deploy

### 6. Verify access control
   - Log out of Google, open URL in incognito → should redirect to Google login
   - Log in with non-whitelisted account → should show "access denied" page
   - Log in with Joan's account → app should load normally

### 7. Add colleagues iteratively
   - For each colleague, repeat step 5: add their Google email to whitelist
   - Communicate the URL + confirm they can access

### 8. Record the final URL
   - Update `dashboard/README.md` with the live URL at the top of the file
   - Commit this update

## Known limitations

### Data freshness
Dashboard only reflects local state pushed to origin. Joan must `git push` after each session for colleagues to see latest state. Max staleness ~24h.

### Free tier RAM
Streamlit Cloud free = 1GB. If universe grows >500 companies, migrate to paid tier.

### OAuth whitelist is manual
No self-service; Joan manages additions/revocations.

## Troubleshooting

### Build fails with "ModuleNotFoundError"
- Check that `dashboard/requirements.txt` includes the missing module.
- Re-deploy after updating requirements.txt.

### Page loads but "Macro data unavailable"
- `load_macro()` calls `tools/macro_fragility.py` via subprocess. On Streamlit Cloud this may fail (no yfinance live connection timeout, or subprocess restrictions). Expected for v1 MVP — the page degrades gracefully.

### yfinance rate-limited
- Cache TTLs (5-60 min) should prevent this for typical traffic. If >10 concurrent users hit the dashboard, consider increasing TTL or migrating to a paid data provider.

### Streamlit Cloud can't find branch
- Confirm `sprint1/foundations` branch is pushed to origin (`git push origin sprint1/foundations`).
- Verify the branch is visible in Streamlit Cloud's branch dropdown when creating the app.

## Post-deploy checklist

- [ ] App URL bookmarked and shared with whitelisted colleagues
- [ ] `dashboard/README.md` updated with live URL
- [ ] `?share=1` param verified working (anonymizes € values)
- [ ] All 4 pages render (Glance, Portfolio, Pipeline, Spanish Funds)
- [ ] Refresh button in sidebar invalidates caches
- [ ] Glossary expander opens correctly
