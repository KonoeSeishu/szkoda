# a = 12
# b = 5

# result = a + b
# result = a - b
# result = a * b
# result = a / b
# result = a // b
# result = a % b
# result = a ** b
# print(result)

capital = 5000
rateOfIntrest = 0.08
inflationRate = 0.15
print("capital:", capital)
print("rateOfIntrest", rateOfIntrest)
print("inflationRate", inflationRate, "\n")


moneyBack = capital + (capital * rateOfIntrest)
print("moneyback:", moneyBack )

moneyMinusInflation = moneyBack - (capital * inflationRate)
print("capital minus inflation", moneyMinusInflation, "\n")

x = 18
x += 2 #x = x + 2
x -= 5 #x = x - 5
x *= 2 #x = x * 2
x %= 4 #x = x % 2
x **= 2
x /= 2
x //= 2

print(x, "\n")

balance = 1000
print("starting balance:",balance,"\n")

balance += 7000
print("money from work:",balance,"\n")

balance -= 2000
print("home rent:",balance,"\n")

balance *= 3
print("BANK ERROR",balance,"\n")

balance -= 4000
print("new computer",balance,"\n")

balance += 4000 / 3 - 4000
print("BANK CORECTION",balance,"\n")

print("ending balance",balance,"\n")

print("Operators:")
print(10 == 5)
print(10 != 5)
print(5 > 2)
print(10 < 2)
print(20 >= 20)
print(20 <= 24)

print("Logical operators")
print(True and True) #T
print(False and False) #F
print(True and False) #F
print(True and False) #F
print(True and False) #T
print(False and False) #T

print(True or True) #T
print(False or True) #T
print(True or False) #T
print(False or False) #F

print(10 > 5 and 3==3) #T
print(4 >= 4 and 4>=12) #Fz

if 12 >= 6 and 5 > 3:
    print(True)

if "al" == "al" or 14 >= 14:
    print(True)


print(not True)
print(not False)

print(not(10==10)) #F

#ex2

age = 12
height = 150

if age >= 10 and height >= 140:
    print("pass")
else:
    print("not pass")


#ownership operators (in, not in)
#they allow to search if value is in data container

listDate1 = [1,2,3,4,5,6]
print(0 in listDate1)
print(4 in listDate1)

print("Jan" in ("Anna", "May", "Bread"))

print(12 not in listDate1)
print(2 not in listDate1)


