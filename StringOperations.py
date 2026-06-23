name = "StarWars"
# Slicing
print(name[0:3])
print(name[2:4])
print(name)
print(name[3])

# Negative Slicing
print(name[-7:-3])
print(name[1:5])

# Slicing with skip value
print(name[2:7:2])

# Advanced
word = "amazing"
print(word[:7])
print(word[1:])

# String function
print(len(word))
print(word.endswith("d"))
print(word.endswith("ing"))
print(word.startswith("A"))
print(word.capitalize())

# Escape Sequence Character
letter = ("hi my name is {your name}\nwhat about you")
print(letter)
letterr = ("hi my name is aryan katoch\n\twhat about you")
print(letterr)
letterrr = ("hi my name is \"aryan katoch\" what about you")
print(letterrr)

# function
print(letter.replace("{your name}","Aryan katoch"))
print(letter)
