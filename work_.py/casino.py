# Нужно написать функцию, котораяф будет возвращать случайные числа из билета от 1 до 1000 
user_input = int(input("Введите случайное число от 1 до 1000: ")) 
import random 
def get_numbers_ticket(min,max, user_inmut): 
    ticet_numbers = set()
    while len(ticet_numbers) < user_inmut:
        ticet_numbers.add(random.randint(min, max))
    return sorted(list(ticet_numbers))
print("Ваши случайные числа: ", get_numbers_ticket(1, 1000, user_input))
