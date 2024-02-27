# @ dekorator wykorzystuje mechanizm funkcji zagnieżdzonej
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    print(fun2)
    return fun2


xFun = fun1()
print(xFun)
print(type(xFun))
xFun()
