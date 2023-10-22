def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

if __name__ == '__main__':
    print(power(2,4))