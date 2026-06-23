def greet(name):
    print("Good Day," + name)
greet("Aryan")

def greety(name,ending = "Thank you"):#by default value of ending ,if not pass any
    print(f"Good Day,{name}")
    print(ending)
greety("Aryan")