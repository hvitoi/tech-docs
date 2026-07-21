# %%
from decimal import Decimal

# Float can't represent 0.1 exactly — Decimal can
0.1 + 0.2 == 0.3  # False  (float is 0.30000000000000004)
Decimal("0.1") + Decimal("0.2") == Decimal("0.3")  # True

# %%
# Always construct from str (or int). Constructing from float inherits float's imprecision.
Decimal(0.1)  # Decimal('0.1000000000000000055511151231257827021181583404541015625')
Decimal("0.1")  # Decimal('0.1')

# %%
# Significant digits are preserved — trailing zeros are NOT stripped
Decimal("1.10")  # Decimal('1.10')
Decimal("1.1")  # Decimal('1.1')
Decimal("1.10") == Decimal("1.1")  # True (equal in value, different in representation)

# %%
# Arithmetic with int works; with float raises TypeError
Decimal("1.5") + 1  # Decimal('2.5')
# Decimal("1.5") + 1.5  # TypeError


# %%
from decimal import Decimal, ROUND_HALF_UP

# quantize: round to a fixed number of decimal places (essential for money)
price = Decimal("19.985")
price.quantize(Decimal("0.01"))  # Decimal('19.98') — round to the nearest even
price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # Decimal('19.99')

# Banker's rounding rounds .5 to nearest even — surprising but reduces bias
Decimal("0.5").quantize(Decimal("1"))  # Decimal('0')
Decimal("1.5").quantize(Decimal("1"))  # Decimal('2')
Decimal("2.5").quantize(Decimal("1"))  # Decimal('2')

# %%
# Money example: 3-way split of $10.00
total = Decimal("10.00")
share = (total / 3).quantize(Decimal("0.01"))  # Decimal('3.33')
remainder = total - share * 3  # Decimal('0.01') — the leftover penny

# %%
# Useful introspection
d = Decimal("12.340")
d.as_tuple()  # DecimalTuple(sign=0, digits=(1, 2, 3, 4, 0), exponent=-3)
d.is_finite()  # True
d.is_zero()  # False

# %%
# Special values: Decimal supports NaN and Infinity
Decimal("Infinity") + 1  # Decimal('Infinity')
Decimal("NaN") == Decimal("NaN")  # False (NaN is never equal to itself)
