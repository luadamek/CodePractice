def pop_last_digit(x):
    '''Pop a digit from the end of x. Assume x is positive.'''
    pop = x % 10
    x = x // 10
    return x, pop

def pop_first_digit(x, order):
    '''Pop the first digit of x. Assume x is positive.'''
    if x < order:
        return x, 0

    first_digit = x // order
    x -= first_digit * order
    return x, first_digit

def get_order(x): #is the number O(11) -- 10, O(101) -- 100 or O(10000) -- 4
    order = 0
    while x >= 10:
        order += 1
        x = x // 10
    return 10 ** order

def helper(x, order):
    if x == 0: return True

    x_without_first, first_digit = pop_first_digit(x, order)
    x_without_last, last_digit = pop_last_digit(x)

    if first_digit != last_digit:
        return False
    else:
        order = order // 100
        x_without_first_and_last, last_digit = pop_last_digit(x_without_first)
        return helper(x_without_first_and_last, order)

def isPalindrome(x):
    if x < 0: return False
    order = get_order(x)
    return helper(x, order)

if __name__ == "__main__":
    print("TESTING")
    assert pop_last_digit(11) == (1, 1)
    assert pop_last_digit(101) == (10, 1)
    assert pop_last_digit(100) == (10, 0)
    assert pop_last_digit(123456) == (12345, 6)
    assert pop_last_digit(0) == (0, 0)
    assert pop_last_digit(1) == (0, 1)

    assert get_order(1) == 1
    assert get_order(0) == 1
    assert get_order(10) == 10
    assert get_order(11) == 10
    assert get_order(123456) == 100000
    assert get_order(123000321) == 100000000

    assert pop_first_digit(11, 10) == (1, 1)
    assert pop_first_digit(323, 100) == (23, 3)
    assert pop_first_digit(2001, 1000) == (1, 2)
    assert pop_first_digit(123000321, 100000000) == (23000321, 1)

    assert isPalindrome(101)
    assert isPalindrome(0)
    assert not isPalindrome(10000)
    assert isPalindrome(10001)
    assert isPalindrome(1001)
    assert not isPalindrome(-101)
    assert not isPalindrome(-2002)
    assert not isPalindrome(-123123)
    assert isPalindrome(123000321)
    assert not isPalindrome(123000123)
    assert isPalindrome(12321)
    assert isPalindrome(20002)
    assert isPalindrome(123000123321000321)

