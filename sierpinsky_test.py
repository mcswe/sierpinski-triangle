import sierpinski

def check_equal(fn_name, expected, result):
    """ Print the outcome of a test. Prints either PASS or FAIL, based
        on whether expected == result, followed by fn_name (the name
        of the function being tested), followed by expected and result
        values. """
    if expected == result:
        outcome = "PASS"
    else:
        outcome = "FAIL"
        
    print(outcome, fn_name, expected, result)


def test_midpoint():
    """ Tests the midpoint function """
    result = sierpinski.midpoint((0, 0), (2, 2))
    expected = (1.0, 1.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 4), (0, 0))
    expected = (2.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((0, 4), (0, 0))
    expected = (0.0, 2.0)
    check_equal("midpoint", expected, result)
    
    result = sierpinski.midpoint((4, 0), (0, 0))
    expected = (2.0, 0.0)
    check_equal("midpoint", expected, result)
    
# write your function here to test one of your functions
# from sierpinski.py

def test_pyththeorem():
    """This tests the pythagorean theorem function I wrote in sierpinski"""
    result = sierpinski.pyth_theorem((2,3),(3,4))
    expected = 1.4142135623730951
    check_equal("pyth_theorem", expected, result)
    
    result = sierpinski.pyth_theorem((1,5),(3,6))
    expected = 2.23606797749979
    check_equal("pyth_theorem", expected, result)
    
    result = sierpinski.pyth_theorem((6,2),(5,9))
    expected = 7.0710678118654755
    check_equal("pyth_theorem", expected, result)
    
    result = sierpinski.pyth_theorem((1,1),(7,4))
    expected = 6.708203932499369
    check_equal("pyth_theorem", expected, result)
    
if __name__ == "__main__":
    
    test_midpoint()
    
    # put a call to your test function here
    test_pyththeorem()
