# diff

- Show diferences between files in `git repository` and `working directory`

```shell
git diff # git repo - WIP
git diff master..HEAD # master - HEAD
```

- Example

```diff
diff --git a/j/javascript.js b/j/javascript.js
index accefce..328daf1 100644
--- a/j/javascript.js
+++ b/j/javascript.js
@@ -1 +1,2 @@
-console.log("Hello World");
+console.log("Henlo World");
+console.log("Another henlo!");
```

- `a` is the previous file
- `b` is the modified file
- `index`: "a" hash file, "b" hash file (to be created) and file permission
- `@@ -1 +1,2 @@`:
  - -1: number of the line in old file
  - +1,2: number of the line in newer file and the length of the block
