


def insert_commas(num):
    num_str = str(num)
    result = ""
    for i, digit in enumerate(num_str[::-1]):
        if i > 0 and i % 3 == 0:
            result = "," + result
        result = digit + result
    return result