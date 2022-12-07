# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

#Объявление переменных
number = int (input('Введите кол-во элементов списка: '))
j = number - 1     #Эта переменная нужна для отслеживая индекса от последнего к первому
numberNew = 0
list = []
listNew = []

#Формирование списка
for i in range (number) :
    list.append (int(input('Введите значение в список: ')))

print (f'Прямая последовательность: {list}') 

#Проверка на чет или нечет кол-ва элементов в исходном списке и присвоение значения для кол-во циклов в новом списке 
if (number % 2 == 0) :
    numberNew = int (number / 2)
else :
    numberNew = (round (number / 2)) + 1

#Формирование обработанного списка
for i in range (numberNew) : 
    listNew.append (list[i] * list[j])
    j -= 1

print (f'Обработанная последовательность: {listNew}') 