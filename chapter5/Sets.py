s = {12, 3, 4, 5, 4, 6, 7,"aryan"}
print(s, type(s))

# Empty set
e = set()
print(type(e))

# methods
s.add(0)
print(s)
s.remove(6)
print(s)
print(len(s))
s.copy()
print(s)
print(s.pop())
s.clear()
print(s)

s1 = {1,2,3,4,56,7,77}
print(s1.union({5,8,0}))
print(s1.intersection({56,2,55,67,3}))
print(s1.issuperset({56,2,7}))
print({56,2}.issubset(s1))
print(s1)



























