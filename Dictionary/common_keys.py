def merge_dicts(dict1, dict2):
    for el in dict2:
        if dict1.get(el):
            dict1[el] = dict1[el] + dict2[el]
        else:
            dict1[el] = dict2.get(el)
    return dict1

if __name__ == '__main__':
        print(merge_dicts({'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))