import pytest
from fuel import gauge, convert
def main():
    ...

def test_e():
    with pytest.raises(ValueError):
        convert("cat.dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    main()