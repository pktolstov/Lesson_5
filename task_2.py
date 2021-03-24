"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('text_file_2.txt', 'r') as my_file:
    count = 1
    stroke = None

    for str in my_file:
        stroke = str.split()
        print(f'в строке: {count}  слов: {len(stroke)}')
        count += 1
