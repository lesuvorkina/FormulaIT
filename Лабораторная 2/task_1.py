money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без
#  долгов
wallet = salary + money_capital - spend # Денег в кошельке
debt = 0 # Долг
month = 1
while wallet >= 0:
    spend = spend+spend*increase
    wallet += (salary - spend)
    if wallet>=0:
        month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)