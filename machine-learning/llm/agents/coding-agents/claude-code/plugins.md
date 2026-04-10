# Claude Plugins

- <https://claude.com/plugins>
- By default, the marketplace `anthropics/claude-plugins-official` is enabled
- Plugins are installed at `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/<namespace>/<plugin_name>/`
  - MCP installed via plugins have its config there, e.g., `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/engineering/mymcp/.mcp.json`
  - MCPs installed via plugins do NOT appear under `~/.claude.json` (mcpServers)

```shell
# Plugins
claude plugin list
claude plugin install "<name>@claude-plugins-official" # or /plugin install <name>@claude-plugins-official
claude plugin uninstall "<name>@claude-plugins-official"

# Marketplace
claude plugin marketplace list
claude plugin marketplace add "git@github.com:myorg/myrepo.git" # add to ~/.claude/settings.json (extraKnownMarketplaces.myorg-myrepo)
claude plugin marketplace update # update plugins list
```
