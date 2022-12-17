from fib import fib

def test():
    assert fib(1) == 1, "Should be 1"
    assert fib(0) == 0, "Should be 0"
    assert fib(6) == 8, "Should be 8"
    print("All tests passed")


test()