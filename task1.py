a = input("Введите номер кредитной карты: ")

def card(a):
    # Проверяем, соотвествует ли ввод формату номера карты
    if len(a) != 16 or not a.isdigit():
        return 'Вы ввели неверный номер карты'
    else:
        return('*'*12 + a[-4:])

print(card(a))





