# Skills

- It's an `open standard`, as the way to provide specialized knowledge to the agent
- <https://agentskills.io/home>
- Skills extend the general knowledge of the LLM
- When invoked, a skill injects a specialized prompt/instruction set into the agent's context
- The [skills](https://www.npmjs.com/package/skills) npm package helps on the setup of skills

```shell
# configure an arbitrary skill
npx skills add "remotion-dev/skills" # it's a github repository! (github.com/remotion-dev/skills)

# check skills updates
npx skills check

# update skills
npx skills update
```

## SKILL.md

- The standard format is a `SKILL.md` file
- The universal location is `~/.agents/skills/` (supported by Codex, Cursor, Opencode), however each agent may have its own location (e.g., `~/.claude/skills/`)

```txt
---
name: commit
description: Create a well-formatted git commit message
---

## Instructions

When the user asks to commit, follow these steps:
1. Run `git diff --staged` to see changes
2. Draft a concise commit message...
```

- The `name` becomes the `/slash-command`, and the description helps the agent decide when to auto-invoke the skill
