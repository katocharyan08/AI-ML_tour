def rm(l,word):
    for item in l:
        l.remove(word)
        return l

l = ["Harry","Shubham","an"]
a = rm(l,"Shubham")
print(a)