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
print(True and False) #m