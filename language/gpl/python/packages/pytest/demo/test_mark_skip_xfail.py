import sys

import pytest


@pytest.mark.skip(reason="not implemented yet")
def test_skipped():
    assert False  # never runs


@pytest.mark.skipif(sys.version_info < (3, 11), reason="needs Python 3.11+")
def test_conditional_skip():
    assert True


# xfail = "expected to fail". The test runs but a failure is not a red CI.
# If it unexpectedly passes, it shows up as XPASS.
@pytest.mark.xfail(reason="known bug, fix pending")
def test_known_failure():
    assert 1 == 2
