from student import Student

students = [Student('eflami', 8),
            Student('patap', 9),
            Student('ernest', 7),
            Student('mihail', 6)]


def calc_sum_scholarship(lst: list):
    summ = 0
    for student in lst:
        summ += student.get_scholarship()
    return summ


def get_exellent_student_count(lst: list):
    count = 0
    for student in lst:
        if student.is_excellent():
            count += 1
    return count


print(f"The summ scholarship: {calc_sum_scholarship(students)}")


print(f"Exellent student count: {get_exellent_student_count(students)}")