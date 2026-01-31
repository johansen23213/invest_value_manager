# Evolution Protocol Skill

## Proceso de cambio
1. DETECTAR problema/mejora
2. PROPONER cambio específico
3. CONFIRMAR con humano (cambios mayores)
4. BACKUP en evolution/backups/{date}/
5. APLICAR cambio
6. REGISTRAR en evolution/changelog.yaml
7. REINICIAR si CLAUDE.md modificado

## Qué puede modificar Claude
- Agentes (.claude/agents/)
- Skills (.claude/skills/)
- CLAUDE.md (con confirmación)
- State files (state/)
- Learning files (learning/)

## Qué NO puede modificar
- settings.json (permisos)
- portfolio/current.yaml (Claude modifica tras confirmación humano)
- config/rules.yaml (reglas fijas)

## Changelog format
```yaml
- id: evo_NNN
  date: YYYY-MM-DD
  type: improvement | bugfix | new_feature | removal
  description: "Qué se cambió y por qué"
  files_changed: [list]
  approved_by: user | auto (minor)
  reversible: true
```

## Seguridad
- Backup SIEMPRE antes de modificar
- Cambios menores (typos, mejoras texto): auto
- Cambios mayores (lógica, nuevo agente): requiere confirmación
- Todo reversible con backup
