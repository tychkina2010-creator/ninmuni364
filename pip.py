while True:
    print("Кулинарный кальткулятор")
    print("\n Действия: + - * / // % ** (или 'выход')")
    print("Выберите действие:")
    print("1 - Сложение (+)")
    print("2 - Вычитание (-)")
    print("3 - Умножение (*)")
    print("4 - Обычное деление (/)")
    print("5 - Целочисленное деление (//)")
    print("6 - Остаток от деления (%)")
    print("7 - Возведение в степень (**)")
    print("0 - Выход из программы")

n = input("Введите номер действия:")
if n == "0":
    print("Работа программы завершена.") 

if i not in ["1", "2", "3", "4", "5", "6", "7"] 
    print("Неверный выбор попробуйте снова.")

a = int(input("Введите первое число:"))
b = int(input("Введите второе число:")) 
if i in ["4", "5", "6"] and b == 0:
    print("Ошибка: делить на ноль нельзя!") 

if n == "1":
    result = a + b
    print(f"Результат: {a} + {b} = {result}")
elif n == "2":
    result = a - b
    print(f"Результат: {a} - {b} = {result}")
elif n == "3":
    result = a * b
    print(f"Результат: {a} * {b} = {result}")
elif n == "4":
    result = a / b
    print(f"Результат: {a} / {b} = {result}")
elif n == "5":
    result = a // b
    print(f"Результат: {a} // {b} = {result}")
elif n == "6":
    result = a % b
    print(f"Результат: {a} % {b} = {result}")
elif n == "7":
    result = a ** b
    print(f"Результат: {a} ** {b} = {result}")


if result is not None and result > 12:
    print("Получится большая порция блюда") 
