# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# new_dict = {new_key:new_value for item in list}
students_scores = {students: random.randint(1, 100) for students in names}
print(students_scores)
# {'Alex': 29, 'Beth': 52, 'Caroline': 90, 'Dave': 15, 'Eleanor': 66, 'Freddie': 50}

# new_dict = {new_key:new_value for (key, value) in dict.items()}
passed_students = {
    student: score for (student, score) in students_scores.items() if score >= 50
}
print(passed_students)
# {'Beth': 52, 'Caroline': 90, 'Eleanor': 66, 'Freddie': 50}
