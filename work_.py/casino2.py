import random 
def get_numbers_ticket(min, max, quantity): 
    try:
        min_num = int(min)
        max_num = int(max)
        quantity_num = int(quantity)
        if min_num < 1 or max_num > 1000:
            return [] 
        if min_num >= max_num:
            return [] 
        if quantity_num < 1 or quantity_num > (max_num - min_num + 1):
            return []
    except ValueError, TypeError:
        return [] 
    ticket_numbers = set()
    while len(ticket_numbers) < quantity_num:
        ticket_numbers.add(random.randint(min_num, max_num))
    return sorted(list(ticket_numbers)) 
#Примеры вызова функции в котором первое применение вызывает ошибку, а второе работает корректно 
print("Ваши случайные числа: ", get_numbers_ticket(10, 5, 10)) 
print("Ваши случайные числа: ", get_numbers_ticket(1, 1000, 5))
        