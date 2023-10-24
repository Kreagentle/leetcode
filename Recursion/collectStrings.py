def collectStrings(obj):
    result = []
    for key, value in obj.items():
        if type(value) is str:
            result.append(value)
        elif type(value) is dict:
            result.extend(collectStrings(value))
    return result


if __name__ == '__main__':
    obj = {
        "stuff": 'foo',
        "data": {
            "val": {
                "thing": {
                    "info": 'bar',
                    "moreInfo": {
                        "evenMoreInfo": {
                            "weMadeIt": 'baz'
                        }
                    }
                }
            }
        }
    }

    print(collectStrings(obj))