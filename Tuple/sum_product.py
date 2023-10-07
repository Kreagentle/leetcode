def sum_product(input_tuple):
    result = 1
    for i in input_tuple:
        result *= i
    return sum(i for i in input_tuple), result