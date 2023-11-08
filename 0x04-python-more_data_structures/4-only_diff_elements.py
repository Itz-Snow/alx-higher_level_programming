#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # create empty sets to hold unique elements from each set
    unique_set_1 = set()
    unique_set_2 = set()
    # iterate over each element in set 1
    for element in set_1:
        # if the element is not in set 2, add to other unique set
        if element not in set_2:
            unique_set_1.add(element)
    # iterate over each element in set 2
    for element in set_2:
        # if the element is not in set 1, add to other unique set
        if element not in set_1:
            unique_set_2.add(element)
    # combine the two unique sets using the union operator
    return unique_set_1.union(unique_set_2)
