def x(a):
    a.append(4)
    print(a)


def y(a):
    a.append(5)
    print(a)


a = [1, 2, 3]
print(x([i for i in a]))
print(y([i for i in a]))
