globalVar = 10

def modifyVariables():
    localVar = 5
    global globalVar 
    globalVar += localVar
    print(globalVar)
    
modifyVariables()
print(globalVar)

#args

def fun(*args):
    print("Parameters count:", len(args))
    for arg in args:
        print(arg)

list = [1,2,6,4,8]

fun(1, list, 3, 5, "xyz", 0)


def fun2(**kwargs):
    print("Parameters count:", len(kwargs)) 
    for key, item in kwargs.items():
        print("key:", key, "Value:", item)

fun2(a=1, b=2, c=3)


def fun2(*args, **kwargs):
    print("Args parameters count:", len(args))
    for arg in args:
        print(arg)
        
    print("Kwargs parameters count:", len(kwargs)) 
    for key, item in kwargs.items():
        print("key:", key, "Value:", item)


fun2(11,21,['x','y','z'], a=10, b=11, c=12)