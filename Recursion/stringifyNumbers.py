def stringifyNumbers(obj):
    object = obj
    for key, value in obj.items():
        if type(value) is int:
            object[key] = str(value)
        elif type(value) is dict:
            object[key] = stringifyNumbers(value)
    return object


if __name__ == '__main__':
    obj = {
        "num": 1,
        "test": [],
        "data": {
            "val": 4,
            "info": {
                "isRight": True,
                "random": 66
            }
        }
    }

    print(stringifyNumbers(obj))