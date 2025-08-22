import random
import statistics

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']

students.sort()

classes = ['Математика', 'Русский язык', 'Информатика']

students_marks = {}

for student in students:
    students_marks[student] = {}

    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(5)]
        students_marks[student][class_] = marks

for student in students:
    print(f'''{student}
            {students_marks[student]}''')



while True:
    print('''
            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Изменить оценки ученика попредмету
            5. Редактирование списка предметов
            6. Редактирование списка учеников
            7. Вывести все оценки ученика
            8. Вывести средний балл ученика
            9. Print best/worst students for every subject
            0. Выход из программы
            ''')
    command = int(input('Введите команду: '))
    if command == 1:

        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in classes:
                counter = int(input("Введите количество оценок для добавления: "))
                for i in range(counter):
                    mark = int(input('Введите оценку: '))
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
            else:
                print("Такого предмета нет")
                continue
        else:
            print("Такого ученика нет")
            continue



    elif command == 2:
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in classes:
                print("1. удалить оценки\n"
                      "2. изменить оценки\n")
                choice = int(input("Введите номер команды: "))
                if choice == 1:
                    counter = int(input("Введите кол-во оценок для удаления: "))
                    print(f"{student} : {class_} : {students_marks[student][class_]}")
                    for i in range(counter):
                        index = int(input("Введите номер оценки для удаления: ")) - 1
                        students_marks[student][class_].pop(index)
                        print(f"{student} : {class_} : {students_marks[student][class_]}")

                elif choice == 2:
                    counter = int(input("Введите кол-во оценок для редактирования: "))
                    print(f"{student} : {class_} : {students_marks[student][class_]}")
                    for i in range(counter):
                        index = int(input("Введите номер оценки для изменения: ")) - 1
                        students_marks[student][class_][index] = int(input("Новая оценка: "))
                        print(f"{student} : {class_} : {students_marks[student][class_]}")
                else:
                    print("Такой команды нет")
            else:
                print("Такого предмета нет")
                continue
        else:
            print("Такого ученика нет")
            continue

    elif command == 5:
            choice = int(input("1. удалить предмет\n"
                               "2. переименовать предмет\n"
                               "3. Add new subject\n"))
            if choice == 1:
                subject = input("Введите название предмета: ")
                if subject in classes:
                    for student in students:
                        students_marks[student].pop(subject)
                    classes.remove(subject)
                    for student in students:
                        print(student, students_marks[student])
                else:
                    print("Такого предмета нет")
                    continue
            elif choice == 2:
                subject = input("Введите название предмета: ")
                if subject in classes:
                    renamed = input("Новое название предмета:")
                    for student in students:
                        for class_ in classes:
                            if subject == class_:
                                temp = students_marks[student][class_]
                                students_marks[student].pop(subject)
                                students_marks[student][renamed] = temp
                    classes[classes.index(subject)] = renamed
                    for student in students:
                        print(student, students_marks[student])
                else:
                    print("Такого предмета нет")
                    continue

            elif choice == 3:
                subject = input("Input new subject's name: ")
                for student in students:
                    students_marks[student][subject] = []
                    print(f"{student} : {students_marks[student]}")
                classes.append(subject)
            else:
                print("Command not found")


    elif command == 6:
        choice = int(input("1. удалить ученика\n"
                           "2. переименовать ученика\n"
                           "3. Add new student\n"))
        if choice == 1:
            name = input("Введите имя ученика")
            if name in students:
                students_marks.pop(name)
                students.remove(name)
            else:
                print("Такого ученика нет")
                continue
            for student in students:
                print(f"{student} : {students_marks[student]}")

        elif choice == 2:
            name = input("Введите имя ученика: ")
            if name in students:
                renamed = input("Введите новое имя ученика: ")
                for student in students:
                    if student == name:
                        temp = students_marks[student]
                        students_marks.pop(student)
                        students_marks[renamed] = temp
                students[students.index(name)] = renamed
                for student in students:
                    print(f"{student} : {students_marks[student]}")
            else:
                print("Такого ученика нет")
                continue

        elif choice == 3:
            newStudent = input("Enter new student's name: ")
            students_marks[newStudent] = {}
            for class_ in classes:
                students_marks[newStudent][class_] = []
            students.append(newStudent)
            students.sort()
            for student in students:
                print(f" {student} : {students_marks[student]} ")
        else:
            print("Command not found")

    elif command == 7:
        name = input("Введите имя ученика для просмотра оценок: ")
        if name in students:
            print(name)
            for subject in classes:
                print(f"{subject} : {students_marks[name][subject]}")
        else:
            print("Такого ученика нет")
            continue
    elif command == 8:
        name = input("Введите имя ученика для просмотра оценок: ")
        if name in students:
            print(name)
            for subject in classes:
                print(f"{subject} : {statistics.mean(students_marks[name][subject])}")

    elif command == 9:
        arrayOfMeans = [] #stores mean grades for every subject for each student
                          #the order of students is identical to the order in students array
        for student in students:
            meanGradeDict = {} # {"subject1" : mean_grade, "subject2" : mean_grade....}
            for class_ in classes:
                meanGradeDict[class_] = statistics.mean(students_marks[student][class_])
            arrayOfMeans.append(meanGradeDict)

        for student in students:
            print(f"{student}\n"
                  f"{arrayOfMeans[students.index(student)]}")

        for subject in classes:
            max_mean_grade = 0
            students_index = 0
            for i in range(len(arrayOfMeans)):
                if max_mean_grade < arrayOfMeans[i][subject]:
                    students_index = i
                    max_mean_grade = arrayOfMeans[i][subject]

            print(f"The best student in {subject} is {students[students_index]} with grade: {max_mean_grade}")

        for subject in classes:
            min_mean_grade = 999999
            students_index = 0
            for i in range(len(arrayOfMeans)):
                if min_mean_grade > arrayOfMeans[i][subject]:
                    students_index = i
                    min_mean_grade = arrayOfMeans[i][subject]

            print(f"The worst student in {subject} is {students[students_index]} with grade: {min_mean_grade}")


    elif command == 0:
        exit()

    else:
        print("Command not found")
        continue


