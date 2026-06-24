with open("log.txt") as f:
    content = f.read()
if "Python".lower() in content.lower():
    print("python is present")
else:
    print("Pyhton is not present")