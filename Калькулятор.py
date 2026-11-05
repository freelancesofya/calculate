print(''' \"Добро пожаловать в простой калькулятор!\"Следуйте инструкциям, нажмите Enter\" ''')
import sys
print(sys.stdin.readline())
print('Начнем')
def get_number(num):
    num='Введите число,нажмите Enter'
    print(num)
    while True:
        try:
            number_str = input() # проверяем, является ли число дробным
            number=float(number_str)
            if number.is_integer():
                return int(number) # проверяем, является ли число целым
            return number
        except ValueError:
            print("Это не число! Пожалуйста, введите число.") # если пользователь ввел не число, то выводим это сообщение
def get_operation(mes):
    operation=input('''Выберите арефметическое действие:
+:Сложение
-:Вычитание
/:Деление
*:Умножение
Ваш выбор:''')
    if operation in ['+','-','/','*']:
        return operation
    else:
        print('Такая операция недоступна.Пожалуйста, выберите +, -, / или *.')
        
def calculate(num1, num2, operation):
    result=None
    if operation == '+':
        result=num1+num2
        print(result)
    elif operation == '-':
        result=num1-num2
        print(result)
    elif operation == '*':
        result=num1*num2
        print(result)
    elif operation == '/':
        try:
            result=num1/num2
        except ZeroDivisionError:
            result="Деление на ноль запрещено"
        else:    
            print('\"Результат:%s\" '%result)
        return result

def main():
    num1 = get_number("Введите первое число: ") # ввод первого числа
    num2 = get_number("Введите второе число: ") # ввод второго числа
    operation = get_operation('Ввод операции') # ввод операции
    result = calculate(num1,num2,operation) # результат

# после выполнения main() запускаем бесконечный цикл (while True)
while True:
    main()
    # спрашиваем пользвователя, желает ли он дальше пользоваться калькулятором
    decision = input('Продолжить? (да/нет): ').lower().strip()
    # если да, то опять вызываем main()
    if decision == 'да':
        main()
    # если нет, выходим из бесконечного цикла (break)
    elif decision == 'нет':
        print("Спасибо за использование калькулятора! До свидания!")
        break
    elif decision != 'да':
          print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")


