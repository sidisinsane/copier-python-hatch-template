def test_template(copie):
    """
    Test the template copying process.

    Args:
        copie: The pytest fixture for copying templates.

    Asserts:
        - The exit code is 0.
        - There is no exception.
        - The project directory exists.
        - The content of the README.rst file is as expected.
    """
    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.rst") as f:
        assert f.readline() == "foobar\n"
