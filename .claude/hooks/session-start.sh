#!/bin/bash
# SessionStart hook - injects system state into Claude's context
# Reads key split files so Claude has context immediately on session start

echo "=== CURRENT DATE ==="
echo "TODAY: $(date '+%Y-%m-%d %H:%M %Z') — USE THIS DATE, NOT MEMORY"
echo ""
echo "=== SYSTEM STATE ==="
head -20 state/system.yaml 2>/dev/null | grep -A2 'last_session:\|status:\|system_version:\|session_number:'

echo ""
echo "=== PORTFOLIO ==="
python3 -c "
import yaml
with open('portfolio/current.yaml') as f:
    d = yaml.safe_load(f)
print(yaml.dump({'cash': d.get('cash'), 'positions': d.get('positions')}, default_flow_style=False, allow_unicode=True))
" 2>/dev/null

echo ""
echo "=== CALENDAR NEXT 14 DAYS ==="
head -60 state/calendar.yaml 2>/dev/null

echo ""
echo "=== MAINTENANCE ==="
grep -A3 'last_health_check:\|next_health_check:\|memory_status:' state/pipeline_tracker.yaml 2>/dev/null
