#!/usr/bin/env python3
"""
Consistency Checker - Framework v4.0
Compara una decisión propuesta contra precedentes similares.

Usage:
  python3 tools/consistency_checker.py "BUY NVO 4%"
  python3 tools/consistency_checker.py "TRIM SHEL.L 50%"
  python3 tools/consistency_checker.py "HOLD ADBE"
"""
import sys
import os
import yaml
import re
from datetime import datetime

def load_decisions_log():
    """Load decisions log from learning/decisions_log.yaml"""
    path = os.path.join(os.path.dirname(__file__), '..', 'learning', 'decisions_log.yaml')
    try:
        with open(path) as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("ERROR: decisions_log.yaml not found")
        return None

def parse_decision(decision_str):
    """Parse a decision string like 'BUY NVO 4%' or 'TRIM SHEL.L 50%'"""
    parts = decision_str.upper().split()
    if len(parts) < 2:
        return None

    action = parts[0]
    ticker = parts[1]
    sizing = parts[2] if len(parts) > 2 else None

    return {
        'action': action,
        'ticker': ticker,
        'sizing': sizing
    }

def find_similar_precedents(decision, log):
    """Find similar decisions in the log"""
    if not log:
        return []

    action = decision['action']
    similar = []

    # Map action to log section
    if action in ['BUY', 'ADD']:
        section = log.get('sizing_decisions', [])
    elif action in ['TRIM', 'SELL', 'EXIT']:
        section = log.get('trim_decisions', [])
    elif action == 'HOLD':
        section = log.get('hold_decisions', [])
    else:
        section = []

    for entry in section:
        entry_action = entry.get('action', '').upper()
        if action in entry_action or entry_action in action:
            similar.append(entry)

    return similar

def calculate_similarity(decision, precedent):
    """Calculate similarity score between decision and precedent"""
    score = 0

    # Same action type
    if decision['action'] in precedent.get('action', '').upper():
        score += 30

    # Same ticker
    if decision['ticker'] == precedent.get('ticker', '').upper():
        score += 40

    # Similar context (tier, etc.)
    context = precedent.get('context', {})
    if context.get('tier') == 'A':
        score += 10  # Boost for Tier A precedents

    # Recency bonus
    try:
        date = datetime.strptime(precedent.get('date', '2020-01-01'), '%Y-%m-%d')
        days_ago = (datetime.now() - date).days
        if days_ago < 7:
            score += 20
        elif days_ago < 30:
            score += 10
    except:
        pass

    return score

def analyze_coherence(decision, precedents):
    """Analyze if decision is coherent with precedents"""
    if not precedents:
        return {
            'coherent': None,
            'message': "No hay precedentes similares para comparar.",
            'note': "Esta será la primera decisión de este tipo."
        }

    # Sort by similarity
    scored = [(p, calculate_similarity(decision, p)) for p in precedents]
    scored.sort(key=lambda x: -x[1])

    top_precedent = scored[0][0] if scored else None

    if not top_precedent:
        return {
            'coherent': None,
            'message': "No hay precedentes suficientemente similares."
        }

    # Compare sizing if available
    if decision['sizing']:
        try:
            new_size = float(decision['sizing'].replace('%', ''))
            prev_size_str = top_precedent.get('sizing', '')
            if '%' in str(prev_size_str):
                prev_size = float(str(prev_size_str).split('%')[0].split()[-1])
                diff = abs(new_size - prev_size)

                if diff <= 1.5:
                    return {
                        'coherent': True,
                        'message': f"Sizing coherente. Diferencia de {diff:.1f}pp vs precedente.",
                        'precedent': top_precedent
                    }
                elif diff <= 3:
                    return {
                        'coherent': True,
                        'message': f"Sizing razonable. Diferencia de {diff:.1f}pp vs precedente. Considerar documentar por qué.",
                        'precedent': top_precedent
                    }
                else:
                    return {
                        'coherent': False,
                        'message': f"ALERTA: Sizing difiere {diff:.1f}pp del precedente. Requiere justificación explícita.",
                        'precedent': top_precedent
                    }
        except:
            pass

    return {
        'coherent': True,
        'message': "Decisión parece coherente con precedentes.",
        'precedent': top_precedent
    }

def print_analysis(decision_str, decision, precedents, coherence):
    """Print formatted analysis"""
    print("=" * 70)
    print("CONSISTENCY CHECK - Framework v4.0")
    print("=" * 70)

    print(f"\nDECISIÓN PROPUESTA: {decision_str}")
    print(f"  Acción: {decision['action']}")
    print(f"  Ticker: {decision['ticker']}")
    if decision['sizing']:
        print(f"  Sizing: {decision['sizing']}")

    print(f"\n{'─' * 50}")
    print("PRECEDENTES SIMILARES:")
    print(f"{'─' * 50}")

    if not precedents:
        print("  (No se encontraron precedentes similares)")
    else:
        for i, p in enumerate(precedents[:3]):  # Top 3
            print(f"\n  #{i+1}: {p.get('ticker', 'N/A')} - {p.get('action', 'N/A')}")
            print(f"      Fecha: {p.get('date', 'N/A')}")
            print(f"      Sizing: {p.get('sizing', 'N/A')}")
            context = p.get('context', {})
            if context:
                print(f"      Tier: {context.get('tier', 'N/A')}, MoS: {context.get('mos', 'N/A')}")
            reasoning = p.get('reasoning', '')
            if reasoning:
                first_line = reasoning.strip().split('\n')[0][:60]
                print(f"      Razón: {first_line}...")

    print(f"\n{'─' * 50}")
    print("ANÁLISIS DE COHERENCIA:")
    print(f"{'─' * 50}")

    if coherence['coherent'] is True:
        print(f"\n  ✓ COHERENTE")
    elif coherence['coherent'] is False:
        print(f"\n  ✗ INCONSISTENCIA DETECTADA")
    else:
        print(f"\n  ? SIN PRECEDENTES COMPARABLES")

    print(f"  {coherence['message']}")

    if 'note' in coherence:
        print(f"\n  NOTA: {coherence['note']}")

    if coherence.get('precedent'):
        p = coherence['precedent']
        print(f"\n  Precedente más relevante: {p.get('ticker')} ({p.get('date')})")

    print(f"\n{'─' * 50}")
    print("RECOMENDACIÓN:")
    print(f"{'─' * 50}")

    if coherence['coherent'] is True:
        print("  → Proceder con la decisión.")
        print("  → Documentar en decisions_log.yaml después de ejecutar.")
    elif coherence['coherent'] is False:
        print("  → PARAR y revisar antes de proceder.")
        print("  → Si el contexto justifica la diferencia, documentar explícitamente.")
        print("  → Si no hay justificación clara, reconsiderar la decisión.")
    else:
        print("  → Esta será un nuevo precedente.")
        print("  → Documentar con detalle el razonamiento.")
        print("  → Las futuras decisiones similares usarán esta como referencia.")

    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    decision_str = ' '.join(sys.argv[1:])
    decision = parse_decision(decision_str)

    if not decision:
        print(f"ERROR: No se pudo parsear la decisión: {decision_str}")
        print("Formato esperado: ACTION TICKER [SIZING]")
        print("Ejemplos: 'BUY NVO 4%', 'TRIM SHEL.L 50%', 'HOLD ADBE'")
        sys.exit(1)

    log = load_decisions_log()
    if not log:
        print("ADVERTENCIA: No se pudo cargar decisions_log.yaml")
        log = {}

    precedents = find_similar_precedents(decision, log)
    coherence = analyze_coherence(decision, precedents)

    print_analysis(decision_str, decision, precedents, coherence)

if __name__ == '__main__':
    main()
