# Firestore

## Security rules

- Define access control logic to the firestore database
- Defined in a `common expression language`
- `firestore.rules`

```rules
match /accounts/{userId} {
  allow read;
  allow write: if request.auth.uid == userId;
}
```
