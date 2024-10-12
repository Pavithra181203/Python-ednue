def merge_dicts(dict1: dict, dict2: dict) :
    merged = dict2.copy()
    merged.update(dict1)
    return merged
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
result = merge_dicts(dict_a, dict_b)
print(result)
