# corpusFJE — Biblioteca d'Agent Skills

**Estat**: productiu (2026-05-17). Format compliant amb [agentskills.io](https://agentskills.io).

Aquesta carpeta conté el coneixement **procedimental** del corpusFJE: com fer
tasques d'adaptació, generació i acompanyament educatiu. Complementa els
fitxers `M*.md` de l'arrel, que contenen el coneixement **declaratiu** (marc
conceptual, perfils, metodologies).

## Estructura

```
skills/
├── adapt-document/      # round-trip de documents (PDF, PPTX, DOCX)
├── complements/         # generació de complements (glossari, preguntes, bastides...)
└── genres/              # escriptura per gènere discursiu (notícia, assaig, conte...)
```

Cada carpeta de skill conté un `SKILL.md` amb:
- **Frontmatter YAML** — `name`, `description`, `agent_role`, `triggers`
- **Cos markdown** — instruccions procedimentals injectades al system prompt

## Activació

Les skills s'activen mitjançant **triggers declaratius** (path + equals/in/exists)
contra el context d'execució (perfil de l'alumne + paràmetres). Tot l'agent
LLM que consumeixi aquesta biblioteca ha d'implementar un loader equivalent a
`skills_loader.py` d'ATNE (~200 línies portable a qualsevol llenguatge).

## Patró canònic corpus ↔ skill

| Tipus | Ubicació | Què | Quan s'injecta |
|---|---|---|---|
| **Marc declaratiu** | `M*.md` (arrel) | Conceptes, perfils, metodologies | A nivell de context permanent |
| **Procedimental** | `skills/*/SKILL.md` | Com fer tasques específiques | Sota demanda quan triggers matchen |

Veure `docs/skills-refactor-plan.md` per al pla complet de Fase E.

## Consumidors actuals

- **ATNE** ([github.com/FundacioJesuitesEducacio/ATNE](https://github.com/FundacioJesuitesEducacio/ATNE)) —
  via `skills_loader.py` amb feature flag `ATNE_USE_SKILLS`.

## Versionatge

Les skills són part del repo corpusFJE. Els canvis segueixen el cicle del
corpus: PR + review pedagògic. Les skills no tenen versionatge semver
individual (per simplicitat); el commit hash del corpusFJE actua com a versió
global de la biblioteca.
