energy_usage = [
    
]

def filter_high_energy_houses(house_energy):
    house_name, energy_values = house_energy
    second_half_energy = energy_values[:6]
    second_half_mean = sum(second_half_energy) / len(second_half_energy)
    return second_half_mean < 1900

low_energy_houses = list(filter(filter_high_energy_houses, energy_usage))
for house in low_energy_houses:
    print(house[0])


words = ['Python']

def order_revenue(order):
    items_total = sum(item[1] for item in order['items'])
    return items_total + order['shipping']

#total_renevue = reduce(lambda total, order: total + order_revenue(order), orders, 0)