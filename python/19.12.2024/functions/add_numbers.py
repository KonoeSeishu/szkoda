def add_numbers(num1, num2):
    result = num1+num2  #local
    return result

c = add_numbers(12,20)
print (c)

a = 34
b = 45
print(add_numbers(a,b))


def add_numbers_3(a, b, c):
    return a+b+c  #local

print(add_numbers_3(1,2,3))

def sub_num(num1,num2):
    return num1-num2


print(sub_num(100, add_numbers(20,25)))

def calc_basket_value(basket_list):
    basket_sum = 0
    for key in basket_list:
        basket_sum += basket_list[key]
    return basket_sum
    
    
shopping_basket = {
    "phone": 1500,
    "TV": 4500,
    "console":2300
}

print(calc_basket_value(shopping_basket))