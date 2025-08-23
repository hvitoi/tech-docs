# %%
from unittest.mock import Mock


mock_function = Mock(return_value="foo")
mock_function()


mock_function.assert_called_once_with()  # ✅
mock_function.assert_called_once_with(1)  # throws
