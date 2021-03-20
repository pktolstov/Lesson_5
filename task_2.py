"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]
"""

from random import randint

list_size = randint(10, 30)
output_list = []
sours_list = [randint(1, 100) for i in range(list_size)]
print(sours_list)
for i in range(len(sours_list)):

    if i != 0 and sours_list[i] > sours_list[i - 1]:
        output_list.append(sours_list[i])
print(output_list)
