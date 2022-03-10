rolls = [1,2,3,4,5,6]
call_cache = {}
def count_rolls(total, n_rolls):
    """
    Count the number of ways that the total from n dice rolls can exceed the total.

    This algorithm runs in (n dice sides - 1) * n ** 2 time, and the proof is:

    The result at each combination f n_rolls and remaining total is cached, so each combination will only be calculated once. How many of these combinations are there?

    (1 roll) has [total - 1, total -6] possibilities. i.e. 6 * 1 - 1 + 1 = 5 + 1
    (2 roll) has [total - 2, total - 12] possibilities. i.e. 6 * 2 - 2 + 1 = 5 * 2  + 1
    (3 roll) has [total - 3, total - 18] possibilities. i.e. 6 * 3 - 3 + 1 = 5 * 3 + 1
    ....
    (n_toll) has [total - n, total - 6 * n] possibilities. i.e. 6 * n - n + 1 = 5 * n + 1

    The total is 5 * (1 + 2 ... n) - 1 = 5 (n(n-1))/2
    Each combination is only calculated once, and hence the complexity is quadratic in O((n_sides - 1) * n ** 2)
    """

    global call_cache
    if (total, n_rolls) in call_cache:
        return call_cache[(total, n_rolls)]

    if n_rolls == 0:
        if total <= 0: return 1
        else: return 0

    elif total <= 0:
        return 6 ** n_rolls

    elif total > 6 * n_rolls:
        return 0

    count = 0
    for roll in rolls:
        count += count_rolls(total - roll, n_rolls - 1)

    if (total, n_rolls) not in call_cache:
        call_cache[(total, n_rolls)] = count

    return count

def calc_prob(total, n_rolls):
    call_cache = {}
    return count_rolls(total, n_rolls) / ( 6 ** n_rolls)

if __name__ == "__main__":
    assert calc_prob(10, 2) == 6 / (6 ** 2) #only way is 6 + 6, 5 + 6, 6 + 5, 5 + 5, 6 + 4, 4 + 6 
    assert calc_prob(11, 2) == 3 / (6 ** 2) #only way is 6 + 6, 5 + 6, 6 + 5
    assert calc_prob(3, 1) == 4/6 #only way is 3, 4, 5, 6
    print(calc_prob(360, 100))

