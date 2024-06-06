from typing import Dict , Union , Optional
import pprint

key = Union[int,str ]
Value = Union[int , str,list,dict,tuple, set]

data : Dict[key ,Value] = {
    "fname":"Ali",
    "name":"Ahmed",
    age: 34 # type: ignore
}

pprint.pprint(data)

# display(data)