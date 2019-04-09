def sum67(nums):
    record = True
    total = 0

    for n in nums:
        if n == 6:
            record = False

        if record:
            total += n
            continue

        if n == 7:
            record = True

    return total
