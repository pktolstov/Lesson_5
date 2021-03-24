"""
Создать вручную и заполнить несколькими строками текстовый файл,
 в котором каждая строка должна содержать данные о фирме:
 название, форма собственности, выручка, издержки.tt
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""
import json

final_list = []
with open('task_7_firms.txt') as my_file:
    profit_firms = {'profit': {}}
    average_profit = {'average_profit': 0}
    losts = {'losts': {}}
    for strings in my_file:
        tmp_list = strings.split()

        if int(tmp_list[-2]) - int(tmp_list[-1]) > 0:

            profit_firms['profit'][tmp_list[0]] = int(tmp_list[-2]) - int(tmp_list[-1])
            average_profit['average_profit'] += (int(tmp_list[-2]) - int(tmp_list[-1]))
        elif int(tmp_list[-2]) - int(tmp_list[-1]) <= 0:
            losts['losts'][tmp_list[0]] = abs(int(tmp_list[-2]) - int(tmp_list[-1]))
    average_profit['average_profit'] /= len(profit_firms['profit'])

    final_list = [profit_firms, average_profit, losts]
    # print(losts, profit_firms, average_profit)
    print(final_list)
with open('task_7.json', 'w') as my_json:
    json.dump(final_list, my_json)
