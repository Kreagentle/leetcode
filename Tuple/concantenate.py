def concatenate_strings(input_tuple):
    result = ''
    for i in input_tuple:
        result += i + ' '
    return result[:-1]
