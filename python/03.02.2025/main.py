from functools import reduce

numbers = [1,2,3,4,5,6]
sum_of_numbers = reduce(lambda x, y:x + y, numbers)
print(sum_of_numbers)


names = ['Ola', 'Ania', 'Kasia']

names_space = list(map(lambda x:x + ' Kowalska', names))
print(names_space)

names_filtred = list(filter(lambda x: len(x) > 12, names_space))
print(names_filtred)