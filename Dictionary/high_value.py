def max_value_key(my_dict):
    result = ''
    tempvalue = -1
    for key,value in my_dict.items():
        if value > tempvalue:
            tempvalue = value
            result = key
    return result


if __name__ == '__main__':
        print(max_value_key({'a': 5, 'b': 9, 'c': 2}))