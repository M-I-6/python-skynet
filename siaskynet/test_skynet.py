"""Skynet SDK tests."""

from . import skynet


def test_walk_directory():
    """Test walk_directory."""
    path = "./testdata/"
    files = skynet.Skynet._Skynet__walk_directory(path)
    print(files)
    expected_files = ["./testdata/file1",
                      "./testdata/dir1/file2",
                      "./testdata/file3"]
    assert len(expected_files) == len(files)
    for expected_file in expected_files:
        assert expected_file in files
