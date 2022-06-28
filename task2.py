# Функция возврашает True, если слово является полиндромом. Иначе False

a = input("Введите любое слово: ")

def polyndrom(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return polyndrom(a[1:-1])

print(polyndrom(a))
