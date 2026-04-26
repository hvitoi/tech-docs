# %%
# __bool__ controls truthiness in `if obj:` and `bool(obj)`.
#
# Fallback chain:
#   1. __bool__   if defined
#   2. __len__    -> True if length > 0
#   3. always True


class Battery:
    def __init__(self, charge):
        self.charge = charge  # percent (0-100)

    def __bool__(self):
        return self.charge > 0


phone = Battery(45)
dead = Battery(0)

bool(phone)  # True
bool(dead)   # False

if phone:
    print("Power on!")
else:
    print("Plug in the charger.")
