# %%
import unittest
# from <module> import <function_to_test>


test_case = unittest.TestCase()

# assertEqual
test_case.assertEqual(1, 1, "asserts that 1 equals 1")

# assertTrue
test_case.assertTrue(1 == 1, "1 equals 1")

# assertFalse
test_case.assertFalse(1 == 0, "1 not equals 0")
