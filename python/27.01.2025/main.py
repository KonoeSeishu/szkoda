def funk(*args):
    x=0
    for i in args:
        x+=i
    return x

print(funk(1,2,3,4))


def funk2(*args, **kwargs):
    print(args)
    for name, age in kwargs.items():
        print(name, age)
         
funk2('Kole',Ewa=33, Ime=44)


