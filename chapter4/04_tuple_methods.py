a = (23,False,45,"harry",45,"potter")
print(a)

# count occurrence of item

print(a.count(45))

# Return first occurrence

print(a.index(45))

t1 = (1,3,4)
t2 = (2,4,"Aryan",5)

# Tuple concatenation

concatenated = t1 + t2
print(concatenated)

# Repetition
rep = a * 2
print(rep)

# Unpacking
Tuple = (1,2,3)
a,b,c = Tuple
print(a,b,c)

# Membership
print(2 in t2)
print(7 in t2)

# length
print(len(t2))
