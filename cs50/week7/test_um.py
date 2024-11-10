from um import*
def main():
    ...

def test_count():
    pass

def count_test():
    assert count("Um, Mum? is this that album where um, umm, the clumsy alums play drums?") == 8
    assert count("Hello, Um world") == 1
    assert count("Um... what are regular expression?") == 1
if __name__ == "__main__":
    main()