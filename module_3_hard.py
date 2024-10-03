
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    result = 0

    def recurse(element):
        nonlocal result
        if isinstance(element, int):
            result += element
        elif isinstance(element, str):
            result += len(element)
        elif isinstance(element, dict):
            for key, value in element.items():
                recurse(key)
                recurse(value)
        else:
            for sub_element in element:
                recurse(sub_element)

    for i in args:
        recurse(i)

    return result



result = calculate_structure_sum(data_structure)
print(result)