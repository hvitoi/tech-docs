

# ---------------------------------------------------------
# Dictionaries

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}
print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Luv"))  # Returns none
print(monthConversions.get("Luv", "Not a valid key"))

del(monthConversions["Apr"])
print(monthConversions)
