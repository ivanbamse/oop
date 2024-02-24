class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

class Mentor(Person):

    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)


class Lecturer(Mentor):

    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def __get_average_grade(self):
        result = 0.0
        grade_total = 0.0
        grade_count = 0
        for grade_item in self.grades.items():
            grade_total += sum(grade_item[1])
            grade_count += len(grade_item[1])
        if grade_count != 0:
            result = grade_total / grade_count
        return round(result, 2)

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __ne__(self, other):
        return self.average_grade != other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __ge__(self, other):
        return self.average_grade >= other.average_grade

    def __str__(self):
        return super().__str__() + f"Средняя оценка за лекции: {self.average_grade}\n"

    average_grade = property(fget=__get_average_grade)

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Student(Person):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __get_average_grade(self):
        result = 0.0
        grade_total = 0.0
        grade_count = 0
        for grade_item in self.grades.items():
            grade_total += sum(grade_item[1])
            grade_count += len(grade_item[1])
        if grade_count != 0:
            result = grade_total / grade_count
        return round(result, 2)

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __ne__(self, other):
        return self.average_grade != other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade

    def __gt__(self, other):
        return self.average_grade > other.average_grade

    def __le__(self, other):
        return self.average_grade <= other.average_grade

    def __ge__(self, other):
        return self.average_grade >= other.average_grade

    def __str__(self):
        return super().__str__() + (f"Средняя оценка за домашние задания: {self.average_grade}\n"
                                           f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\n"
                                           f"Завершенные курсы: {','.join(self.finished_courses)}\n")

    average_grade = property(fget=__get_average_grade)

