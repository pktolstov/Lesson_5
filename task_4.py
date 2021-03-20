"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
 Сформировать итоговый массив чисел, соответствующих требованию.
 Элементы вывести в порядке их следования в исходном списке.
 Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
from random import randint
new_list= [randint(1,30) for i in range(randint(20,30))]
origin_list=[]
print(new_list)
for i in range(len(new_list)):
    #print(new_list.count(new_list[i]))
    if new_list.count(new_list[i])==1:
        origin_list.append(new_list[i])
print(origin_list)
