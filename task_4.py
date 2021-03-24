"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
ru_numerals = ['Один', 'Два', 'Три', 'Четыре']
with open('task_4_eng_numeral.txt') as my_file:
    task_4_ru_numeral = open('task_4_ru_numeral.txt', 'w')
    count = 0
    for i in my_file:
        print(f'{ru_numerals[count]} - {i.split()[2]}', file=task_4_ru_numeral)

        count += 1
    task_4_ru_numeral.close()
