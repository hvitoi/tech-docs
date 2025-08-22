# Timing Attacks

- Let's imagine some attackers are trying to guess the username and password.
- And they send a request with a username `john` and a password `123`.

```python
# name=john; password=123
if name == "henry" and password == "abc":
```

- Right at the start it compares `j` with `h` and returns False right away, because it already knows that the strings are not equal
- If the attacker tries again with `henri`, the application will take longer, so it will take some extra microseconds to reply back "Incorrect username or password"
- At that point, by noticing that the server took some microseconds longer to send the "Incorrect username or password" response, the attackers will know that they got something right, some of the initial letters were right.
- Fix it with `secrets.compare_digest()`
