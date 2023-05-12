get_student_names = {
    "Студент 1": "Артём",
    "Студент 2": "Иван",
    "Студент 3": "Роман"}

tuple_of_students = ()

def student_names():
    tuple_of_students = tuple(sorted(get_student_names.values()))
    return tuple_of_students
print(student_names())