def check_same_frequency(list1, list2):
    dict1 = {i: list1.count(i) for i in list1}
    dict2 = {i: list2.count(i) for i in list2}
    return dict1 == dict2
