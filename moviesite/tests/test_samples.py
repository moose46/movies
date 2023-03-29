# from django.test import TestCase
import os
from pathlib import Path
import sqlite3

import pytest


# Create your tests here.


class DataFileNames:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __repr__(self) -> str:
        return self.filename

    def __eq__(self, other: str) -> bool:
        self.filename == other


@pytest.fixture
def session():  # 1
    connection = sqlite3.connect(":memory:")

    db_session = connection.cursor()

    yield db_session

    connection.close()


@pytest.fixture
def setup_db(session):  # 2
    session.execute(
        """CREATE TABLE numbers

                          (number text, existing boolean)"""
    )

    session.execute('INSERT INTO numbers VALUES ("+3155512345", 1)')

    session.connection.commit()


@pytest.fixture
def base_path() -> Path:
    """Get the current folder of the test"""
    return Path(__file__).parent


@pytest.mark.usefixtures("setup_db")
def test_db(session):
    """
    https://smirnov-am.github.io/pytest-testing_database/
    https://www.geeksforgeeks.org/sql-using-python/
    """
    session.execute("select count(*) from numbers")
    count = session.fetchone()
    print(f"\n ************** count = {count[0]}")
    assert count[0] == 1


def test_something(base_path: Path, monkeypatch: pytest.MonkeyPatch):
    print(f"+++ base_path = {base_path}")
    monkeypatch.chdir(base_path)
    # Do something in the data folder


@pytest.fixture
def sample_home() -> Path:
    # return b"C:\Users\me\VsCodeProjects\movies\moviesite\moviesite"
    print(os.getenv("PYTEST_CURRENT_TEST"))
    print(f"\n*** sample_home() = {Path.home()}")
    return Path.home()


@pytest.fixture
def sample_file():
    """return an existing file"""
    print(f"*** sample_file {Path.cwd()}")
    return (
        Path.home()
        / "VsCodeProjects"
        / "movies"
        / "moviesite"
        / "moviesite"
        / "requirements.txt"
    )


# @pytest.mark.skip
def test_foo(sample_home):
    assert sample_home.is_dir()


# @pytest.mark.skip
def test_is_a_file(sample_file):
    assert sample_file.is_file()


# @pytest.mark.skip
def test_home(sample_home):
    assert sample_home == Path.home()


# @pytest.mark.skip
def test_is_a_wildcard_file(sample_home):
    # sample_path = Path.cwd() / "moviesite"
    cnt = 0
    test_dir = sample_home / "VsCodeProjects" / "movies" / "moviesite" / "moviesite"

    for s in test_dir.glob("s*.py"):
        print(s)
        if s.exists():
            cnt += 1
    assert cnt > 0


# test_is_a_wildcard_file()
# print(f"sample_home = {sample_home}")
