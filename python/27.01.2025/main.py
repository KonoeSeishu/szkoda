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



#lambda

def add_one(x):
    return x + 1

def kw(parametr):
    return parametr * parametr

print(add_one(5))
print(kw(8))

def func(f, number):
    return f(number)

func(add_one, 10)