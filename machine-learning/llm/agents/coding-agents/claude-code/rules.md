# Claude Rules

## CLAUDE.md

- A Markdown file that Claude Code automatically reads at the start of every session
- The `/init` command analyzes your codebase and generates an initial CLAUDE.md
- Keep it lean (< 200–300 lines) and move heavy details into rules, skills, or reference docs

- **Global**: `~/.claude/CLAUDE.md`
- **Project**: `.claude/CLAUDE.md`, `./CLAUDE.md`

- For the project memory, focus on what Claude cannot infer from the code:
  - Build, test, and deploy commands
  - Architectural decisions and business rules
  - Naming conventions and explicit prohibitions
  - Links to internal documentation

## Rules

- **Global**: `~/.claude/rules/`
- **Project**: `.claude/rules/`

- Allows you to organize instructions into multiple focused files instead of piling everything into CLAUDE.md
- Rules can be `scoped by path` (via frontmatter paths:), loading only when Claude is working on files that match a specific pattern
