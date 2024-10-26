salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
# Метод полного перебора
money_capital=spend-salary
month=1
spend_test=spend
while month<10:
    money_capital += 1
    spend_test=spend
    wallet = salary + money_capital - spend_test # Денег в кошельке
    month = 1
    while wallet >= 0:
        spend_test = spend_test+spend_test*increase
        wallet += (salary - spend_test)
        if wallet>=0:
            month += 1
money_capital -= 1
print(f"Подушка безопасности, чтобы протянуть {month} месяцев без долгов:", money_capital)