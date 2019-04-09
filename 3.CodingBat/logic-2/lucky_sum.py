def lucky_sum(a, b, c):
    total = 0

    for n in (a, b, c):
        if n != 13:
            total += n
        else:
            break

    return total
