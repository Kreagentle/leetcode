obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nestedEvenSum(obj, sum=0):
    for key, value in obj.items():
        if type(value) is int and value%2==0:
            sum += value
        elif type(value) is dict:
            sum += nestedEvenSum(value)
    return sum


if __name__ == '__main__':
    print(nestedEvenSum(obj1))
    print(nestedEvenSum(obj2))