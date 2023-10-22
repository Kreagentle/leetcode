def isPalindrome(strng):
    if len(strng) < 1:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])

if __name__ == '__main__':
    print(isPalindrome("apple"))