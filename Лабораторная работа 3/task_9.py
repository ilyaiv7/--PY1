salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(1, 11):
    if i == 1:
        delta = spend - salary
    else:
        spend *= 1.03
        delta = spend - salary
    need_money += delta

print(round(need_money))
