per_cent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}
list_per_cent = list(map(float,per_cent.values()))
deposit_sum = int(input("Введите сумму вклада:"))
profit = list(map(int,[deposit_sum * i/100 for i in list_per_cent]))
print("Ваш профит в разных банках через запятую:", profit)
print("Максимальный профит:", max(profit),"руб")


