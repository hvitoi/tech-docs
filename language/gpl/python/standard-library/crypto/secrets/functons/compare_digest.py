# %%
import secrets

# Protects against Timing Attacks
secrets.compare_digest("a", "a")  # True
