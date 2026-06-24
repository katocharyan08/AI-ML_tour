f = open("Poem.txt")
content = f.read()
if "Twinkle".lower() in content.lower():
    print("Twinkle is present in the content")
else:
    print("not present")
f.close()