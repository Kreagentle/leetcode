def filter_dict(my_dict, condition):
    return {key:value for key,value in my_dict.items() if condition(key, value)}