import pyexcel
from collections import OrderedDict

data = [
    OrderedDict({
        "Name":"Quân",
        "age":22,
        "city":"hanoi",
    }),
    OrderedDict({
        "Name":"hồng",
        "age":12,
        "city":"hanoi",
    }),
    OrderedDict({
        "Name":"Huy",
        "age":22,
        "city":"hanoi",
    }),
]
pyexcel.save_as(records=data,dest_file_name="your_file.xls")