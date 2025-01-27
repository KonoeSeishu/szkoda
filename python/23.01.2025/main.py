def addEmployess(email, salary):
 employ = {
     "email": email,
     "salary": salary
 }
 
addEmployess("ania@test.com", 6000)
addEmployess("adam@test.com", 8000)
addEmployess("kasia@test.com", 10000)

def increaseSalary(employess, pctIncrease):
    pctIncrease *= 0.01
    for e in employess:
        e["salary"] *= 1 + pctIncrease

#ncreaseSalary(employess, 20)
#print(employess)