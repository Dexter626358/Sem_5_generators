"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
 имена str, ставка int, премия str с указанием процентов вида «10.25%».
  В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


names = ["Alice", "Bob", "Charlie", "Eve", "Frank"]
rates = [1000, 2000, 3000, 4000, 5000]
bonuses = ["10.25%", "5.75%", "12.50%", "8.00%", "15.00%"]

generator_sum = {name: rate * float(bonus[0:-1]) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(generator_sum)
for key, value in generator_sum.items():
    print(f"{key} : {value}")