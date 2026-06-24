
with open("log.txt") as f:
    lines = f.readlines()

lineno= 1
for line in lines:
    if "Python".lower() in line.lower():
        print(f"python is present in line no {lineno}")
    lineno+=1
else:
    print(f"Pyhton is not present in line no. {lineno}")