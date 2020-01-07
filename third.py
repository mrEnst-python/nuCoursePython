'''
Задание к уроку № 3
'''
# Считать текст из файла. Создан файл thirdLessonText.txt, куда скопирован текст из задания.
# from typing import TextIO
from string import punctuation
# для задачи PRO
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

text = open('thirdLessonText.txt', 'r')  # type: TextIO
text = text.read()  # считать из файла в текстовую переменную

#Задания
# 1) методами строк очистить текст от знаков препинания;
# знаки препинания - punctuation из модуля string
punctuation += "—»«" #+знаки, нет в наборе punctuation из модуля, но есть в тексте, их тоже надо убрать
# и что делать с этим? - француженкою-гувернанткой, заменить дефис на пробел??
text = text.replace('-', ' ') #заменим на пробел
cleanText = ''.join(x for x in text if x not in punctuation)  #очистить от знаков препинания

#2) сформировать list со словами (split);
wordList = cleanText.split()

#3) привести все слова к нижнему регистру (map);
wordList = list(map(lambda x: x.lower(), wordList))
for i in range(len(wordList)):
    lemma = morph.parse(wordList[i])[0]
    print(wordList[i], ' - ', lemma.normal_form) #вывести слово и его лемму, на повторения не обращаем внимания

#3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

wordDict = {} #make new empty dict
for i in range(len(wordList)):
    wordDict[wordList[i]] = wordList.count(wordList[i]) #fill dict with word as a key and word count as a value
# lets sort it to make more frequent words go higher
# from StckOverflow exmple of sorting by values
import operator
x = wordDict
wordDict = sorted(x.items(), key=operator.itemgetter(1), reverse = True)
#have no idea how it works... and it sorts ascending, but i wanted descending!...
#you must use reverse = True to get it descending :-))) it's tha simple :-)

# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
# wordDict уже отсортирован, нужно вывести первые 5, это и будут наиболее употребимые слова
print('5 наиболее употребимых в тексте слов: (\'<Слово>\', <количество>)')
for i in range(5):
    print(wordDict[i])
# количество разных слов - длина списка уникальных слов (set)
print('Количество уникальных (разных) слов в тексте', len(set(wordList)))
print('Уже интересно! Скоро можно будет на дзене статьи сочинять :-)))')
