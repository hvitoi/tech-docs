# Movements

- `h`: left
- `l`: right
- `k`: up
- `j`: down

- `0` or `^`: beginning of line
- `$`: end of line

- `w`: next word (first char)
- `ge`: previous word (last char)
- `e`: current word (last char) or next word (last char)
- `b`: current word (first char) or last word (first char)

- `f[char]`: next occurrence of a character. E.g., fz (next z)
- `F[char]`: previous occurrence of a character. E.g., fz (previous z)

- `*`: next occurrence of the word under cursor
- `#`: previous occurrence of the word under cursor

- `%`: alternate between opening and closing characters. E.g., ( and ), [ and ], { and }

- `gg`: go to first line
- `25%`: go to the line at 25% of the file
- `50%`: go to the line at 50% of the file
- `G`: go to last line
- `8G`: go to line number 8

- `{`: previous empty line
- `}`: next empty line

- `''`: return to the previous position

- `Ctrl` + `g`: shows current position
- `Ctrl` + `u`: half page up
- `Ctrl` + `d`: half page down

- **Movement powered**
  - Commands can be added any number multiplier in front of it
  - `<>[n][action/movement]`
  - Examples
    - 3w (next 3 words)
    - 3igo (insert gogogo)
    - dw deletes from cursor to beginning of next word
    - d2e deletes from cursor to the end of next word

- **Movement around**
  - `<>aw`: for word
  - `<>ap`: for paragraph
  - `<>a(`: for parenthesis

- **Movement inside**
  - `<>iw`: for word
  - `<>ip`: for paragraph
  - `<>i(`: for parenthesis

- **Movement until**
  - `<>t/`: until the slash
  - `<>t.`: until the dot

> gg + 0 + v + G: selects the whole file
