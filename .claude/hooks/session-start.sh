#!/bin/bash
# SessionStart hook - injects system state into Claude's context
# Reads key files so Claude has context immediately on session start

echo "=== SYSTEM STATE ==="
head -80 state/system.yaml 2>/dev/null | grep -A2 'last_session:\|status:\|system_version:'

echo ""
echo "=== PORTFOLIO ==="
head -55 portfolio/current.yaml 2>/dev/null

echo ""
echo "=== CALENDAR NEXT 14 DAYS ==="
grep -A6 'date: 2026-0[2-3]' state/system.yaml 2>/dev/null | head -40

echo ""
echo "=== MAINTENANCE ==="
grep -A3 'last_health_check:\|next_health_check:\|memory_status:' state/system.yaml 2>/dev/null
