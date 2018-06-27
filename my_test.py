import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

def test_func():
    assert func(4) == 5

def func(x):
    return x + 1

if __name__ == "__main__":
    test_func()
    test_mytest()