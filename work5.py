# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int (input('Введите число: '))
fibo_numbers = []
a = 1
b = 1

#шаги в положительную сторону
for i in range(number) :
    fibo_numbers.append(a)
    a, b = b, a + b

#обнуляем переменные для отрицательного подсчета
a = 0
b = 1

#шаги в отрицательную сторону
for i in range (number + 1) :
    fibo_numbers.insert(0, a)
    a, b = b, a - b

print (f'Список Фибоначчи для числа {number}:')
print (fibo_numbers)