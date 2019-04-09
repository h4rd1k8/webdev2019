def count_code(str):
    return sum(1 for i in range(len(str) - 3)
        if str[i:i + 2] == 'co' and str[i + 3] == 'e'
    )