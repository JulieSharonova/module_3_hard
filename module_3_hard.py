data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    summ = 0
    for i in data_structure:
        if isinstance(i, dict):
            summ += calculate_structure_sum(i.items())
        elif isinstance(i, (list, set, tuple)):
            summ += calculate_structure_sum(i)
        elif isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
    return summ
