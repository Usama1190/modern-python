from typing import Dict

my_dic: Dict[any, any] = {
    10: "Ten",
    "seven": 7,
    (1, 2, 3): [1, 2, 3]
}


from typing import Dict

my_optional_dic: Dict[any, optional[int]] = {
    1: "one",
    "seven": None,
    (1, 2, 3): [1, 2, 3]
}

print(my_optional_dic)
