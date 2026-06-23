marks = {
    "harry" : 100,
    "kala" : 67
}
# print(marks["kala"], type(marks))

# Methods
print(marks.items())
marks.update({"kala" : 77})
print(marks["kala"])
print(marks.keys())
print(marks.get("harry"))
# print(marks["friends"])
print(marks.get("friends"))
print(marks.pop("harry"))
print(marks.popitem())

print(len(marks))