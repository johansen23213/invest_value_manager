# 📈 Value Investor System

Sistema **autónomo** de inversión value que **aprende, evoluciona, y se reprograma a sí mismo**.

## 🎯 Principio

```
Claude → Gestor del fondo. Decide, aprende, mejora, se modifica.
Tú     → Propietario. Confirmas operaciones y cambios al sistema.
```

## 🧬 Auto-Evolución

Claude puede modificarse a sí mismo:

```
✅ Puede modificar:
   • Sus prompts (.claude/commands/*.md)
   • Sistema core (CLAUDE.md)
   • Crear nuevos comandos
   • Eliminar comandos obsoletos

❌ No puede modificar:
   • Permisos del sistema
   • Tu portfolio
   • Reglas fijas de inversión
```

**Ejemplo:**
```
Tú (3 veces): "Los análisis son muy largos"

Claude detecta → propone cambio → tú confirmas → Claude se modifica
→ "Reinicia Claude Code para aplicar"
```

## 🧠 Aprende de la Experiencia

```
Inversión cerrada → Lección → Ajusta parámetros
Tu feedback       → Detecta patrón → Modifica su código
Errores repetidos → Crea regla → Evoluciona
```

## 💾 Memoria a Largo Plazo

```
CAPA 1: Activa (~30KB)      → Siempre cargada
CAPA 2: Reciente (~50KB)    → Bajo demanda  
CAPA 3: Archivo (ilimitado) → Compactado
```

## 🚀 Comandos

```bash
/macro              # Análisis macro + geopolítico
/analyze TICKER     # Analizar empresa
/review             # Revisar portfolio
/decide             # Decisiones de inversión
/learn              # Aprendizaje
/compact            # Gestión de memoria
/evolve             # Auto-modificación del sistema
```

## 📁 Estructura

```
value-investor/
├── .claude/commands/        # 🧬 Claude puede modificar estos
├── CLAUDE.md                # 🧬 Sistema core (modificable)
├── evolution/               # Historial de cambios al sistema
│   ├── changelog.yaml
│   └── history/             # Backups antes de cada cambio
├── state/system.yaml
├── learning/
├── archive/
├── portfolio/current.yaml   # 👤 Solo tú
├── thesis/
├── world/
└── journal/
```

## ✅ Tu rol

1. Confirmar operaciones de inversión
2. Confirmar cambios al sistema (cuando Claude propone)
3. Actualizar portfolio cuando operas en eToro

## 🔄 Resiliencia Total

- Todo en archivos → reinicio seguro
- Calendario de eventos → nada se olvida
- Aprendizaje continuo → mejora con el tiempo
- Compactación automática → funciona años
- Auto-evolución → se adapta y mejora su propio código
