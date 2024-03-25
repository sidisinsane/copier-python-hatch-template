def test_template(copie):
    result = copie.copy()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.rst") as f:
        assert f.readline() == "foobar\n"
