'''
Домашнее задание к уроку 4 (функции)
1. Напишите функцию (F): на вход список имен и целое число N;
на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения: количество имен 20, N = 100,
рекомендуется использовать функцию random);

2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
'''

# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random);
from random import randrange


def f(namesList, n):
    newNamesList = []  # new empty list
    for i in range(n):
        newNamesListIndex = randrange(0, len(
            namesList))  # get random number to take value from namesList parameter
        newNamesList.append(namesList[newNamesListIndex])
    return newNamesList


l = ['Dima', 'Natasha', 'Olga', 'Fedor', 'Vasily', 'Evgeny']
print(f(l, 20))
print(f(l, 100))

from collections import Counter


def mostCommon(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]


print('Most common name among random 20 is ', mostCommon(f(l, 20)))
print('Most common name among random 100 is ', mostCommon(f(l, 100)))


# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def countItemFreq(lst):
    """
    Принимает на вход список, считает частоту элементов и делает словарь
    Возвращает отсортированный по возрастанию словарь
    :param lst: список на вход
    :return: отсортированный по возрастанию словарь
    """
    d = {}
    for item in lst:
        if (item in d):
            d[item] += 1
        else:
            d[item] = 1
    return sorted(d, reverse=False)


print("Самая редкая буква, с которой начинается имя из 100 - ",
      countItemFreq(f(l, 100))[0][0])

# для задания PRO
# 4.  В файле с логами найти дату самого позднего лога (по метке времени):
# алгоритм:
# прочитать файл с логом в массив, осортировать по времени (первый элемент), вывести самый поздний
import datetime
from collections import OrderedDict

f = open("log", "r")
lines = {}  # new empty list for lines from log file
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

for line in f:
    l = line.split(' - ')
    date_time_obj = datetime.datetime.strptime(str(l[0]), '%Y-%m-%d %H:%M:%S,%f')
    #print(type(date_time_obj), date_time_obj)
    lines[date_time_obj] = l[1:]
f.close()
print(lines)
d = OrderedDict(sorted(lines.items(), key=lambda t: t[0]))
print(type(d), d)
latest = len(d) - 1
print('The latest log entry is this: ', list(d)[latest], d[list(d)[latest]])
# как-то по тупому вышло, как оптимизировать, подскажите!?