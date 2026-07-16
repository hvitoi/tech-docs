# Visualizing SQLite

## Desktop

- `DB Browser for SQLite` (aka *sqlitebrowser*) — the classic free GUI: browse data, edit rows, build queries, ER-ish schema view
  - <https://sqlitebrowser.org>
  - `brew install --cask db-browser-for-sqlite`
- `TablePlus` — polished, multi-DB, freemium (<https://tableplus.com>)
- `DBeaver` — free, Java, multi-DB, has an ER diagram view (<https://dbeaver.io>)
- `Beekeeper Studio` — open source, nice UX (<https://beekeeperstudio.io>)

## VS Code

- `SQLite Viewer` (qwtel) — click a `.db` file and it opens as a table
- `SQLTools` + `SQLTools SQLite` driver — query editor with results grid

## Web / shareable

- `Datasette` — points at a `.db` and serves a browsable, JSON-API'd, publishable website. Best tool for **exploring and sharing** a read-only dataset
  - <https://datasette.io>
  - `uvx datasette serve mydb.db --open`
  - `datasette publish cloudrun mydb.db` to deploy it
  - plugins: `datasette-cluster-map`, `datasette-vega` (charts)
- `sqlite-web` — Flask-based admin UI, allows writes (<https://github.com/coleifer/sqlite-web>)
  - `uvx sqlite-web mydb.db`
- `sqlime` / `SQLite Playground` — run SQLite in the browser via WASM (<https://sqlime.org>)

## Schema diagrams

- `sqlite3 mydb.db .schema` piped into <https://dbdiagram.io> or `schemacrawler`
- `SchemaSpy` — generates an HTML site with ER diagrams (needs Graphviz)

## Terminal

- `.mode box` / `.mode markdown` in the `sqlite3` shell is often enough — see [cli.md](cli.md)
- `harlequin` — a TUI SQL IDE (<https://harlequin.sh>), `uvx harlequin mydb.db`
- `visidata` — spreadsheet-in-the-terminal, opens `.db` files directly (`vd mydb.db`)
- `litecli` — sqlite3 shell with autocompletion + syntax highlighting (<https://litecli.com>)
