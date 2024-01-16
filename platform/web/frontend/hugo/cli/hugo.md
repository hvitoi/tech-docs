# hugo

```shell
# build the website on the current folder
hugo # compile to `build/`
```

## new

```shell
# New content (uses default archetype)
hugo new "foo.md" # creates content/foo.md

# Site boilerplate
hugo new site <site-name>

# Theme
hugo new theme <theme-name>

# Content
hugo new content "<sectionname>/<filename>.<format>"
```

## server

```shell
# Serve
hugo server

#
hugo server --buildDrafts

# Force complete refresh
hugo server --noHTTPCache
```
