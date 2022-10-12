money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

wallet = money_capital

while wallet >= spend:
    wallet -= spend
    spend *= 1.05
    month += 1
    wallet += salary

print(month)
