# tmp_path is a pathlib.Path to a fresh empty directory unique
# to each test. pytest cleans it up automatically.


def test_writes_file(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("world")
    assert file.read_text() == "world"


def test_isolated_from_other_tests(tmp_path):
    # this tmp_path is a different directory than the one above
    assert list(tmp_path.iterdir()) == []
