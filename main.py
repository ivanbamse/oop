import education
import random

def scather_students_courses(students, courses):
    for student in students:
        student.courses_in_progress = courses[:]
        for i in range(4):
            actual_length = len(student.courses_in_progress)
            i_random = random.randint(0, actual_length - 1)
            finished_course = student.courses_in_progress.pop(i_random)
            student.finished_courses += [finished_course]

def scather_mentors_courses(mentors, courses):
    for mentor in mentors:
        courses_count = random.randint(2, 5)
        mentor.courses_attached = random.sample(courses, courses_count)[:]

def rate_lecturers(students, lecturers):
    for student in students:
        for lecturer in lecturers:
            for course in lecturer.courses_attached:
                student.rate_lecturer(lecturer, course, random.randint(7, 10))

def rate_students(students, reviewers):
    for reviewer in reviewers:
        for student in students:
            for course in student.courses_in_progress:
                reviewer.rate_hw(student, course, random.randint(6, 10))

def print_students_info(students):
    if len(students) > 0:
        print(f"\nСТУДЕНТЫ\n")
        best_student = students[0]
        for student in students:
            print(student)
            if student > best_student:
                best_student = student
        print(f"{'_'*50}\nЛучший студент: {best_student.name} {best_student.surname}\nСредняя оценка: {best_student.average_grade}\n{'_'*50}")

def print_mentors_info(mentors):
    if len(mentors) > 0:
        is_lecturer_type = True if isinstance(mentors[0], education.Lecturer) else False
        print(f"\n{'ЛЕКТОРЫ' if is_lecturer_type else 'ЭКСПЕРТЫ'}:\n")
        if is_lecturer_type:
            best_lecturer = mentors[0]
        for mentor in mentors:
            print(mentor)
            if is_lecturer_type:
                if mentor > best_lecturer:
                    best_lecturer = mentor
        if is_lecturer_type:
            print(f"{'_' * 50}\nЛучший лектор: {best_lecturer.name} {best_lecturer.surname}\nСредняя оценка: {best_lecturer.average_grade}\n{'_' * 50}")

def average_grade_of_course(persons, course):
    if len(persons) > 0:
        is_lecturer_type = True if isinstance(persons[0], education.Lecturer) else False
        grade_total = 0.0
        grade_count = 0
        result = 0.0
        for person in persons:
            if course in person.grades:
                grade_total += sum(person.grades[course])
                grade_count += len(person.grades[course])
        if grade_count > 0:
            result = grade_total/grade_count
        return round(result, 2)

def print_courses_grades(persons, courses):
    if len(courses) > 0:
        is_lecturer_type = True if isinstance(persons[0], education.Lecturer) else False
        print(f"\nОбщая статистика по {'лекторам' if is_lecturer_type else 'студентам'}\n")
        for course in courses:
            avg_grade = average_grade_of_course(persons, course)
            if avg_grade > 0.0:
                print(f"- Курс: {course}\n  средняя оценка: {avg_grade:.2f}")

if __name__ == '__main__':

    courses = ['C++', 'Java', 'JavaScript', 'Python', 'Django', 'Bitrix', 'Android']

    students = []
    students += [education.Student('Антон', 'Высоцкий', 'муж.')]
    students += [education.Student('Валерия', 'Беляева', 'жен.')]
    students += [education.Student('Дарья', 'Спиридонова', 'жен.')]
    students += [education.Student('Милана', 'Иванова', 'жен.')]
    students += [education.Student('Мирослава', 'Чеснокова', 'жен.')]
    students += [education.Student('Эмилия', 'Кузнецова', 'жен.')]
    students += [education.Student('Алексей', 'Клюев', 'муж.')]
    students += [education.Student('Юлия', 'Фролова', 'жен.')]
    students += [education.Student('Мирон', 'Алексеев', 'муж.')]
    students += [education.Student('Михаил', 'Колесников', 'муж.')]
    students += [education.Student('Дарья', 'Киселева', 'жен.')]
    students += [education.Student('Даниил', 'Токарев', 'муж.')]
    students += [education.Student('Михаил', 'Поляков', 'муж.')]
    students += [education.Student('Роман', 'Кондрашов', 'муж.')]
    students += [education.Student('Ника', 'Гурова', 'жен.')]

    lecturers = []
    lecturers += [education.Lecturer('Кирилл', 'Смирнов')]
    lecturers += [education.Lecturer('Вадим', 'Дмитриев')]
    lecturers += [education.Lecturer('Анна', 'Анисимова')]
    lecturers += [education.Lecturer('София', 'Егорова')]
    lecturers += [education.Lecturer('Иван', 'Цветков')]

    reviewers = []
    reviewers += [education.Reviewer('Елена', 'Рожкова')]
    reviewers += [education.Reviewer('Арсений', 'Бондарев')]
    reviewers += [education.Reviewer('Иван', 'Барсуков')]
    reviewers += [education.Reviewer('Юлия', 'Сидорова')]
    reviewers += [education.Reviewer('Юрий', 'Носков')]

    scather_students_courses(students, courses)
    scather_mentors_courses(lecturers, courses)
    scather_mentors_courses(reviewers, courses)

    rate_students(students, reviewers)
    rate_lecturers(students, lecturers)

    print_mentors_info(reviewers)
    print_mentors_info(lecturers)
    print_students_info(students)
    print_courses_grades(lecturers, courses)
    print_courses_grades(students, courses)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
