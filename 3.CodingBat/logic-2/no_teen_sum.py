def no_teen_sum(a, b, c):
    nums = (a, b, c)
    return sum(fix_teen(n) for n in nums)


def fix_teen(n):
    return 0 if n not in (15, 16) and 13 <= n <= 19 else n