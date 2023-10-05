def count_word_frequency(words):
    dictionary = dict()
    for i in words:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

if __name__ == '__main__':
    print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))