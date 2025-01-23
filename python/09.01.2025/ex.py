def incraseSalary(money, bonus):
    money += money*0.2
    return money + bonus

salary = 5000

newSalary = incraseSalary(salary, 1000)

print("salary: ", salary)
print("newSalary: ",newSalary)



employee =  {
    "name": "Jan",
    "email": "jan@wp.pl",
    "rank": "programmer",
    "salary": 8000
}

def promoteToManager(user):
    if ["rank"] == "manager":
        print("worker already manager")
        return
    elif ["rank"] != "manager":
        employee["rank"] = "manager"
        employee["salary"] *= 1.5 
        
promoteToManager(employee)

print([employee])