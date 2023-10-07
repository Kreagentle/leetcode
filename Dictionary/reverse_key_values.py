def reverse_dict(my_dict):
    result = {}
    for key, value in my_dict.items():
        result[value] = key
    return result

if __name__ == '__main__':
        print(reverse_dict({'a': 5, 'b': 9, 'c': 2}))