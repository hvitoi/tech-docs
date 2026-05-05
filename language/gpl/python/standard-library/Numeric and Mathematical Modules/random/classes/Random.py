# %%
import random

# Isolated RNG — same API as the module, doesn't touch global state
seed = random.Random(42)

seed.random()
seed.randint(1, 10)
seed.uniform(0.0, 1.0)
seed.choice(["a", "b", "c"])
seed.choices([1, 2, 3], k=5)
seed.sample(range(100), k=3)

deck = [1, 2, 3, 4, 5]
seed.shuffle(deck)

# %%
# Independent from the global RNG: seeding one doesn't affect the other
random.seed(0)
seed = random.Random(999)
seed.random()  # rng's stream
random.random()  # global stream — undisturbed

# %%
# Reseed mid-stream
seed.seed(123)
