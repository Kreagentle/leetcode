def reverse(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse(string[:-1])

if __name__ == '__main__':
    print(reverse("apple"))