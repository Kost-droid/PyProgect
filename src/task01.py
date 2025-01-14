# # # # import cowsay
# # # # my_fish = r''
# # # # cowsay.draw ('my fish', my_fish)
# # #
# # # data = ["name:Alice", "age:25", "city:New York"]
# # # person = {value.split(":")[0]: value.split(":")[1] for value in data}
# # #
# # print ({**{1: 2,2: 3, 3: 4}, **{2: 5, 3: 4}})
#
# my_dict = {1:'a', 2:'b',3: {4:'c', 5: 'e'}}
#
# # for key, value in my_dict.items():
# #     if type (value) == dict:
# #         for key_i, value_i in value.items():
# #             print (f'{key} --> {key_i}: {value_i}')
# #     else:
# #         print(f'{key}: {value}')
#
# def iter_dict (d: dict):
#     for key, value in d.items ():
#         if type (value) == dict:
#             iter_dict (value)
#         print(f'{key}: {value}')
#
# iter_dict(my_dict)
#
#
#
#
# У вас есть список с данными о студентах, где каждый студент представлен в виде строки в формате "имя:оценка".
# Например: ["Аня:5", "Боб:4", "Света:5", "Аня:4", "Боб:5"].
#
# Создание словаря:
# Сформируйте словарь, где ключами будут имена студентов, а значениями — списки
# их оценок. Например, после обработки данными результат должен выглядеть так:

list_studens  =["Аня:5", "Боб:4", "Света:5", "Аня:4", "Боб:5"]
megazin = {value.split(":")[0]: [] for value in list_studens}
for key in megazin.keys():
    for value in list_studens:
        if key == value.split(":")[0]:
            megazin.get(key).append(int (value.split(":")[1]))


#      {
#        "Аня": [5, 4],
#        "Боб": [4, 5],
#        "Света": [5]
#      }
# Добавление оценок:
# Реализуйте функцию, которая принимает имя студента и оценку, и добавляет эту оценку в соответствующий список оценок
# в словаре. Если студента нет в словаре, создайте новую запись.
#
def result_lesson (name: str, numer: int):
    if name in megazin:
        megazin.get(name).append(numer)
    else:
        megazin[name] = [numer]

result_lesson("Maria", 5)
result_lesson("Света", 5)


def average_grade (name: str, magazin: dict) -> float:
    grades = magazin.get(name)
    average_grades = 0
    for grade in grades:
        average_grades+=grade
    return average_grades / len (grades)

print (average_grade('Аня', megazin))

def best_student (magazin: dict) -> str:
    best = ''
    for key, value in magazin.items():
        if best == '':
            best = key
        else:
            if average_grade (best, megazin) < average_grade (key, megazin):
                best = key
    return best


print (megazin)
print(best_student(megazin))

# Расчет среднего балла:
# Напишите функцию, которая принимает имя студента и возвращает средний балл этого студента.
# Поиск лучшего студента:
# Реализуйте функцию, которая находит студента с наивысшим средним баллом и возвращает его имя.
# Условия:
# Учите, что при добавлении оценок не следует изменять существующие оценки в словаре. Все оценки должны храниться по тем же именам,
# что и были изначально.
# Попробуйте самостоятельно выполнить это задание, используя операции со словарями, такие как добавление элементов, доступ по ключу и итерация. Удачи!

















