def flatten(arr):
    result = []
    for item in arr:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

if __name__ == '__main__':
        print(flatten([1, [2, [3, 4], [[5]]]]))