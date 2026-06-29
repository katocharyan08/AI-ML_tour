def demo():
    try:
        a = int(input("Enter a number : "))
        print(a)
        return
    except Exception as e:
        print(e)
        return

    finally:
        print("Finally always execute")

demo()