def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

if __name__ == '__main__':
        print(capitalizeWords(['car', 'taco', 'banana']))