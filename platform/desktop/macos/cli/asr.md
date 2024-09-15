# asr

- `Apple Software Restore` copies volumes (e.g. from disk images)
- There is only one tool that can successfully copy the `Signed System Volume` (SSV), and that is `Apple Software Restore (ASR)`
- Copies full MacOS installations, including
  - System volume
  - Data volume
  - Preboot content
  - Recovery content
- <https://discussions.apple.com/docs/DOC-250005828>

## restore

```shell
# Clone stub OS without blessing
asr restore \
  --source diskIDofStubSystemVol \
  --target diskIDofMacosContainer \
  --no-personalization
```
