def count_evens(nums):
    return sum(1 for n in nums if n % 2 == 0)