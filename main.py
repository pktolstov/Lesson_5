from task_1 import staff_salary
from sys import argv

# try:
file,work_hours, rate, bonus = argv


# except ValueError:
# print('Invalid arguments')
# exit()

print(staff_salary(int(work_hours), int(rate), int(bonus)))
