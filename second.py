'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('Задача 1')
i = 0
while i < 5:
    print( i, ': 0', sep='')
    i += 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Задача 2')
i = 0
fives = 0
while i < 10:
    number = input('Введите цифру:')
    if int(number) == 5: fives += 1
    i += 1
print('Вы ввели ', fives, 'цифр 5')
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
result = 1
for i in range(1,10):
    result *= i
print(result)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
number = 123456789
number = str(number)
for i in range(0, len(number)):
    print(number[i])

'''
Задача 6
Найти сумму цифр числа.
'''
number = 12345
sum = 0
number = str(number)
for i in range(0, len(number)):
    sum += int(number[i])
print(sum)

'''
Задача 7
Найти произведение цифр числа.
'''
number = 12345
mult = 1
number = str(number)
for i in range(0, len(number)):
    mult *= int(number[i])
print(mult)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
number = 123465
number = str(number)
for i in range(0, len(number)):
    if int(number[i]) == 5:
        print('Yes')
        break
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
number = 123459
maxi = 0
number = str(number)
for i in range(0, len(number)):
    if int(number[i]) > maxi : maxi = int(number[i])
print(maxi)

'''
Задача 10
Найти количество цифр 5 в числе
'''
number = 125346555
number5Count = 0
number = str(number)
for i in range(0, len(number)):
    if int(number[i]) == 5:
        number5Count += 1
print('Всего чисел 5 в числе', number, '-', number5Count)
