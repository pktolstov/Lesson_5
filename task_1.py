"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def staff_salary(total_work_hours, rate_hour, addition_bonus):
    try:
        return total_work_hours * rate_hour + addition_bonus
    except:
        TypeError
        return

# print(staff_salary(20,20,20))
