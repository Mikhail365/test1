count = int(input("Введите количество покупаемых билетов:\n"))
result = 0
for i in range(1,count + 1):
    old = int(input("Введите количество полных лет " + str(i) + '-го посетителя:\n'))
    if old < 18:
        result += 0
    elif 18 <= old < 25:
        result += 990
    else:
        result += 1390
if count >= 3:
    result *= 0.9
print("Cумма заказа: " + str(result) + " руб")