from functools import reduce

l = [13,435,56,23,604,45,65,78,70]

def max(a,b):
    if a > b:
        return a
    return b

print(reduce(max,l))