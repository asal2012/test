from numb3rs import validate
import pytest
def main():
    test()

def test():
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("199.911.288.882") == False
    assert validate("149.249.249.249") == True
    assert validate("1.555.555.555") == False
    
if __name__ == "__main__":
    main()