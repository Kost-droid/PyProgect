from operator import truediv
import math


# выводит информацию о всех студентах в удобочитаемом формате (имя, фамилия и средняя оценка).
def print_students (students):
    [massages (f'{x[0]} {x[1]} {average_score(x[2])}') for x in students]


def average_score (scores: list):
   return round (sum(scores) / len(scores),1) if scores else 0


def student_is_exist (students, student_name, student_lastname):
    return any(x[0] == student_name and x[1] == student_lastname for x in students)


def student_get_index (students, student_name, student_lastname):
    index = - 1
    while index < len (students):
        index +=1
        print (index)
        if students[index][0] == student_name and students[index][1] == student_lastname:
            break
    return index



# добавляет нового студента в список. Функция принимает имя, фамилию и список оценок.
def add_new_student (students: list, new_student_name = None, new_student_lastname  = None):
    if  new_student_name is None or new_student_lastname is None:
        new_student_name = input_and_validator('', flag = False,
                                               inputs_massage = 'Input new student name ', error_massage='Incorrect value')
        new_student_lastname = input_and_validator('', flag = False,
                                                   inputs_massage = 'Input new student lastname ', error_massage='Incorrect value')
    if student_is_exist (students, new_student_name, new_student_lastname):
        if choice('A student is exist. Update ?'):
            add_new_student(students, new_student_name, new_student_lastname)
    else:
        students.append((new_student_name, new_student_lastname, []))
        update_students_scores(students, new_student_name, new_student_lastname)
        massages('A new student Add')


def update_students_scores(students,  student_name, student_lastname):
    students_scores = []
    continues = ''
    while continues != 'exit':
        continues = input_and_validator('1', '2', '3', '4', '5', flag=True,
                                           inputs_massage='Input score ', error_massage='Incorrect value')
        if continues != 'exit':
            students_scores.append(int (continues))

    students[student_get_index (students, student_name, student_lastname)] = (student_name, student_lastname, students_scores)

# выбор пользователя
def choice (massage):
    massages (massage)
    action = input_and_validator('y', 'n', flag=True, inputs_massage = 'Input action y/n ', error_massage='Incorrect value')
    return action


#удаляет студента по имени и фамилии из списка
def del_student (students):
    student_name = input_and_validator('', flag=False, inputs_massage='Input student name ',
                                       error_massage='Incorrect value')
    student_lastname = input_and_validator('', flag=False, inputs_massage='Input student lastname ',
                                           error_massage='Incorrect value')
    if not student_is_exist(students, student_name, student_lastname):
        massages('Student is not exists !')
    else:
        del students[student_get_index(students, student_name, student_lastname)]
        massages('Student dell !')



#обновляет оценки студента, принимает имя, фамилию и новый список оценок.
def update_student (students: list, student_name = None, student_lastname = None ):
    student_name = input_and_validator('', flag = False, inputs_massage = 'Input student name ', error_massage='Incorrect value')
    student_lastname = input_and_validator('', flag = False, inputs_massage = 'Input student lastname ', error_massage='Incorrect value')
    if not student_is_exist(students, student_name, student_lastname):
        if choice('A student is not exist. Append ?'):
            add_new_student (students, student_name, student_lastname)
    else:
        update_students_scores(students, student_name, student_lastname)
        massages('Student update !')


def input_and_validator (*args, flag, inputs_massage, error_massage):
    result_validation = False
    while not result_validation :
        try:
            user_action = input(inputs_massage)
            if (user_action in args) == flag or user_action == 'exit':
                result_validation = user_action
        except TypeError:
            pass
        if not result_validation:
            massages (error_massage)

    return result_validation


def massages (massage):
    print (massage)

# # основное меню, которое позволяет пользователю выбрать одно из действий
# Просмотреть всех студентов
# Добавить студента
# Удалить студента
# Обновить оценки студента
# Выйти из программы.


def main_menu ():
    action = input_and_validator('1','2','3','4','5', flag = True, inputs_massage = '1. Просмотреть всех студентов '
                                                                                     '2. Добавить студента 3. Удалить студента '
                                                                                     '4. Обновить оценки студента 5. Выйти из программы \n '
                                                                                     'Input action ', error_massage ='Incorrect value' )
    return action


def main ():
    students = [('Иван', 'Иванов', [3, 2, 5]), ('Анна', 'Петрова', [4, 3, 6])]
    stop = True
    while stop:
        action = main_menu()
        if action == '1':
            print_students(students)
        elif action == '2':
            add_new_student(students)
        elif action == '3':
            del_student(students)
        elif action == '4':
            update_student(students)
        else:
            stop = False
    else:
        massages('Good by !!!')



main()
