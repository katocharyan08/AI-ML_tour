# readlines() and readline()

f = open("File.txt")

lines = f.readlines()

print(lines , type(lines))

f.close()

f = open("File.txt")

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
line5 = f.readline()
print(line5 == "")

f.close()

f = open("File.txt")
line = f.readline()
while line != "":
    print(line , type(line))
    line = f.readline()

f.close()


