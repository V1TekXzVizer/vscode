def first(size,*args):
    return size + len(args)
    print(first)

first(1, 2)


def second(size,**kwargs):
    return size + len(kwargs)
    print(second)

second(1, a=2, b=3) # spasibo nahuj
