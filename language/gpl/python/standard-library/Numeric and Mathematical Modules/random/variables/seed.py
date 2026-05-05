# %%
import random
# Seeds the Global RNG! (use the Random class if you just want to receive a PRNG, instead of modifying the global RNG)

# A pseudo-random number generator (PRNG) is a deterministic function that produces a sequence of numbers that look random.
# a seed affects not only the random() function but all the other random-related functions (e.g., choice, randint, etc)

random.seed(42)  # seeds the global RNG
random.random()  # 0.6394267984578837
random.random()  # 0.025010755222666936

random.seed(42)  # seeds the global RNG
random.random()  # 0.6394267984578837 - same!
random.random()  # 0.025010755222666936 - same!

# %%

random.seed()  # OS-based, unpredictable (the default)
random.random()

random.seed()
random.random()  # not same
