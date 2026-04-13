# Google Workspace MCP

```shell
cd ~
git clone git@github.com:gemini-cli-extensions/workspace.git
cd workspace

npm install
npm run build

claude mcp add --transport stdio google-workspace -- node ~/dev/workspace/workspace-server/dist/index.js
```

- You should rebuilt to update

```shell
cd ~/dev/workspace
git pull
npm install
npm run build
```
