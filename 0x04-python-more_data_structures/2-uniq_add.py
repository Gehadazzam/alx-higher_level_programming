#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    for num in my_list:
        uniq.add(num)
    return sum(uniq)
