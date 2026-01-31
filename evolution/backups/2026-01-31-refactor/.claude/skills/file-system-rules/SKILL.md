# File System Rules Skill

## Autoridad
El file-system-manager es la ÚNICA autoridad sobre ubicación de ficheros.

## Estructura de directorios
```
value-investor/
├── state/                    # Estado del sistema
│   ├── system.yaml           # Cerebro principal
│   ├── agent_coordination.yaml # Coordinación agentes
│   └── file_moves.yaml       # Log de movimientos
├── portfolio/
│   ├── current.yaml          # Claude modifica tras confirmación humano
│   └── validations/          # Validaciones committee
├── thesis/
│   ├── active/               # Con posición abierta
│   ├── watchlist/            # Listos para comprar
│   └── research/             # En análisis
├── world/
│   ├── current_view.md       # Visión macro actual
│   ├── geopolitics.md        # Geopolítica
│   └── updates/              # Updates específicos
├── journal/
│   ├── decisions/            # Decisiones compra/venta
│   ├── reviews/              # Revisiones
│   └── log/                  # Actividad sistema
├── learning/
│   ├── lessons.yaml          # Lecciones
│   ├── key_learnings.md      # Resumen clave
│   └── system_config.yaml    # Config evolutiva
├── archive/                  # Memoria largo plazo
│   ├── index.yaml
│   ├── investment_history.md
│   ├── thesis/closed/
│   └── decisions/
├── evolution/
│   ├── changelog.yaml
│   └── backups/
└── config/
    └── rules.yaml            # READ-ONLY
```

## Reglas
- portfolio/current.yaml: Claude puede modificar SOLO tras confirmación del humano
- NUNCA eliminar sin archivar
- SIEMPRE registrar movimientos en state/file_moves.yaml
- Thesis sigue flujo: research → watchlist → active → archive/closed
