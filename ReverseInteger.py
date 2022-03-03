import math

def pop_digit(x):
    """
    Takes an integer x, removes the final digit, and returns a tuple of x and the final digit.
    If x is negative, x and the popped digit are both negative.

    Parameters
    ----------

    x : int
        The number from which to pop the final digit

    Returns
    -------
        a tuple of (x, d) where x has it's final digit removed, and d is the final digit
    """

    if x >= 0:
        pop = x % 10
        x = x // 10

    if x < 0:
        pop = (x % 10)
        if pop > 0: pop -= 10
        x = (x-1) // 10 + 1
    return x, pop

def push_digit(x, d):
    """
    Takes an integer x and a digit d, and returns a new integer with digit d appended.

    Parameters
    ----------

    x : int
        The number to append digit d to

    d : int
        The digit to be appended to x

    Returns
    -------
        a tuple of (x, d) where x has it's final digit removed, and d is the final digit
    """
    x = 10 * x + d
    return x

def reverse(x):
    """
    Takes an integer x and reverses it. However, if the integer overflows, return 0.
    The integer overflows if it is outside of the range [-2^31, 2^31-1]. You cannot
    store any integer in memory that overflows, even though python might allow it.

    Parameters
    ----------

    x : int
        The integer to be reversed

    Returns
    -------
        The reverse of the integer, or 0 if the reverse overflows
    """
    pos = x >= 0
    neg = not pos
    INTMAX = 2147483647 #2^31 - 1
    INTMIN = -2147483648 # -2**31
    rev = 0

    while x != 0:
        x, d = pop_digit(x)

        #-----------------x is positive-------------------------
        #
        #does the push cause overflow?
        #A)
        #overflow -> INTMAX < 10 * rev + d -> INTMAX // 10 <= rev
        #therefore: INTMAX // 10 > rev -> no overflow
        #
        #B)
        #no overflow -> INTMAX >= 10 * rev + d -> INTMAX // 10 >= rev
        #therefore: INTMAX // 10 < rev -> overflow
        #
        #C) 
        #INTMAX // 10 = rev -> rev = 214748364. Then it overflows if d > 8 (positive) 
        #-------------------x is negative------------------------
        #
        #does the push cause overflow?
        #A)
        #overflow -> INTMIN > 10 * rev - d -> INTMIN // 10 >= rev - 1
        #therefore: INTMIN // 10 < rev - 1 -> no overflow

        #B)
        #nooverflow -> INTMIN <= 10 * rev - d -> INTMIN // 10 <= rev - 1
        #therefore: INTMIN // 10 > rev -1 -> overflow

        #C)
        #INTMIN // 10 == rev - 1 --> rev = -2147483640 + d. Then it only overflows if d < -8

        if (pos):
            if (INTMAX // 10 > rev): rev = push_digit(rev, d)
            elif (INTMAX // 10 < rev): return 0
            else:
                #rev = 2147483640 + d (d > 7 is a problem)
                if d > 7: return 0
                rev = push_digit(rev, d)
        else:
            if (INTMIN // 10 < rev - 1):
                rev = push_digit(rev, d)
            elif (INTMIN // 10 > rev - 1):
                return 0
            else:
                #rev = -2147483640 + d (d < -8 is a problem)
                if d < -8: return 0
                rev = push_digit(rev, d)

    return rev


if __name__ == "__main__":
    assert pop_digit(100009) == (10000, 9)
    assert pop_digit(1) == (0, 1)
    assert pop_digit(0) == (0, 0)
    assert pop_digit(10) == (1, 0)
    assert pop_digit(1000000000) == (100000000, 0)
    assert pop_digit(-11) == (-1, -1)
    assert pop_digit(-101) == (-10, -1)
    assert pop_digit(-1) == (0, -1)
    assert pop_digit(-10) == (-1, 0)
    assert pop_digit(-100) == (-10, 0)

    assert push_digit(123, 3) == 1233
    assert push_digit(135, 0) == 1350
    assert push_digit(0, 9) == 9
    assert push_digit(1, 9) == 19
    assert push_digit(1, 0) == 10
    assert push_digit(-10, -7) == -107
    assert push_digit(-100, -9) == -1009


    assert reverse(2147483647) == 0
    assert reverse(214748364) == int(str(214748364)[::-1])
    assert reverse(0) == 0
    assert reverse(1) == 1
    assert reverse(10) == 1
    assert reverse(-211) == -112
    assert reverse(-1) == -1
    assert reverse(-2147483648) == 0
    assert reverse(-2147483649) == 0
    assert reverse(-214748364) == -1 * int(str(214748364)[::-1])
    assert reverse(-10) == -1
    assert reverse(-20000) == -2

    assert reverse(1463847412) == 0
