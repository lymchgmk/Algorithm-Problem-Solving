def y(x):
    global a
    a = 4
    return 0


def f(a):
    a = 3
    print(a)
    return a

a = 5
f(a)
print(a)
y(a)
print(a)