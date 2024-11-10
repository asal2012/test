from bank import value
def test_value_hello():
    assert value("hello") == 0
    assert value("hello newman") == 0
    assert value("HeLLO") == 0
    assert value("Hello newman") == 0
    assert value("hheelloo") == 0
    assert value("HeLLO") == 0

def test_value_h():
    assert value("Hi") == 20
    assert value("how you doing") == 20
    assert value("hi") ==20
    assert value("How you doing") == 20
    assert value("hey you") == 20
    assert value("helo") == 20

def test_value_other():
    assert value("what's happening") == 100
    assert value("What's happining") == 100
    assert value("Cs50") == 100
    assert value("Cs") == 100
    assert value("50") == 100
    assert value("50cs") == 100