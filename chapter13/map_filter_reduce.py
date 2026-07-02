from functools import reduce

# MAP

l = [1,2,3,4,5,6]

square = lambda x : x*x

sqlist = map(square,l)

print(list(sqlist))

# FILTER

def even(n):
    if n % 2 == 0:
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

# LAMBDA

sum = lambda a,b : a+b
mul = lambda a,b : a*b

print(reduce(sum,l))
print(reduce(mul,l))
