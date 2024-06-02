#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(Guido):
    greeting = f"Hello, {Guido}!"
    print(greeting)
    pass

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")
    pass

def add(num1, num2):
    return num1 + num2

def test_add():
    result = add (45, 55)
    assert result == 100
    pass

def halve(number):
    return number / 2

def test_halves():
    result_int = halve(100)
    assert result_int == 50

    result_float = halve(99.0)
    assert result_float ==49.5
    pass
