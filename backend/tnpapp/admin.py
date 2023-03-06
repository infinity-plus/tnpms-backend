from typing import Tuple, Any
from copy import deepcopy


def append_primary_fields(
    data: Tuple[Any, ...],
    # data: Tuple[Any, ...],
    new_fields=Tuple[str, ...],
):
    tmp_data = deepcopy(data)
    tmp_data[0][1]["fields"] = (*tmp_data[0][1]["fields"], *new_fields)
    return tmp_data


# def append_primary_fields(
#     data: Tuple[Any, ...],
#     new_fields=Set[str],
# ):
#     tmp_data = copy(data)
#     tupleset = set(tmp_data[0][1]["fields"]).union(new_fields)
#     tmp_data[0][1]["fields"] = tuple(tupleset)
#     return tmp_data
