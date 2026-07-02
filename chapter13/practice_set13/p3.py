l = [13,435,56,23,60,45,65,78,70]

def div(n):
    if n % 5 == 0:
        return True
    return False

result = filter(div,l)
print(list(result))