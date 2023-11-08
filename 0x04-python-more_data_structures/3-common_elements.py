#!/usr/bin/python3
def common_elements(set_1, set_2):
    # create an empty set to hold common elements
    c_set = set()
    # iterate over each element in set 1
    for element in set_1:
        # if the element is also in set 2, add it to the common set
        if element in set_2:
            c_set.add(element)
    # return the set of common elements
    return c_set
