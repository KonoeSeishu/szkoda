number = 15

if number > 5:
    print(str(number))
    if number >= 10:
        print(str(number))
    print("end")



#Z

age = 18
weight = 50

if age>=18:
    if(weight>50):
        print("person can give blood")
    else:
        ("person can't give blood bc of the weight")
else:
    print("person can't give blood bc of the age")


experience = 2
languages = ["python", "typescript", "javascript", "java"]
contractType = "b2b"

if(experience>=2 and "python" in languages and "java" in languages):
    print("")

    if(contractType=="b2b" or contractType=="employment"):
        print("everything is alright")
    else:
        print("no no no")
else:
    print("you leak 2 years of experience or language ")


data = True

if data == True:
    print("true")

if data is True:
    print("true")

if data:
    print("true")



data1 = False

if data1 != True:
    print("false")


raining = False
haveUmbrella = False
temperature = 14

if(temperature>=40 or temperature<0):
    print("Stay at home")

elif(temperature>0 & temperature<10 & haveUmbrella):
    print("Use Umbrella")

elif(not raining & temperature>=10):
    print("DO NOT use Umbrella")

else:
    print("Stay at home")


#isinstance

number = 1.0

if(isinstance(number, int)):
    print("YES")
else:
    print("NO")

password = "cskdnjcasa#!"

if (len(password) >= 11 and "!" in password):
    print("good")


