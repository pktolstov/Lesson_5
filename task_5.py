"""
5. Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('task_5.txt', 'w+') as my_file:
    my_file.write(input('Введите числа через пробел>>> '))
with open('task_5.txt') as my_file_read:
    tmp_list_read=my_file_read.readline().split()
    print(sum(int(i) for i in tmp_list_read))
