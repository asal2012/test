from working import convert
import pytest
def main():
    test_convert()

def test_convert():
    with pytest.raises(ValueError):
        convert("9:00 am 5:00 pm")
    with pytest.raises(ValueError):
        convert("9:00 am - 5:00 pm")
    with pytest.raises(ValueError):
        convert("9:00 am to 5:00 pm")
    assert convert("9 am to 5 pm") == ("09:00 am 17:00")
    assert convert("5:30 am to 6:30 pm") == ("5:30 am to 18:30 pm")

if __name__ == "__main__":
    main()