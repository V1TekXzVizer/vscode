#Щоб виграти головний приз лотереї, 
# необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
# Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.



import random  
 
def get_numbers_ticket (min, max, quantity): 
    ticket_numbers = set()
    while len(ticket_numbers) < quantity: 
        ticket_numbers.add(random.randint(min, max)) 
    return sorted(list(ticket_numbers)) 
print("Вы получили следующие номера билета:", get_numbers_ticket(1, 1000, 6)) 