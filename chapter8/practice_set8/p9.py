def rm(l,word):
    n = []
    for item in l:
        n.append(item.strip(word))
    return n

l = ["Harry","Shubham","an"]
print(rm(l,"Harry"))
