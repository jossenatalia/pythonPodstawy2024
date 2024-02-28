def allparams(a, b, /, c=42):
    print('a, b', a, b)
    print('c', c)


def allparams2(a, b, /, c=42, *args, d=256):
    print('a, b', a, b)
    print('c, d', c, d)
    print('args', args)

def allparams3(a, b, /, c=42, *args, d=256, **kwargs):
    print('a, b', a, b)
    print('c, d', c, d)
    print('args', args)
    print('kwargs', kwargs)


allparams(1, 2)
allparams(1, 2, c=3)

# / odziela argumenty, które muszą być przekazane pozycyjne od niepozycyjnych
print("-------------")
allparams2(1, 2, 5)
allparams2(1, 2, c=8)
allparams2(1, 2, c=8, d=0)
# jeśli chcemy przekazać do argsów wartości, c musi być po pozycji, na końcu d musi być po nazwie
allparams2(1, 2, 3, 1, 2, 3, 4, d=15)
print("Parameters 3")
allparams3(1, 2, 3, 1, 2, 3, 4, d=15, name="Radek", a=10)


