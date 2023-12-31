import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

for key, value in student_dict.items():
    print(key)  # student # score
    print(value)  # ["Angela", "James", "Lily"] # [56, 76, 98]

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#   student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

# Loop trough a data frame:
for key, value in student_data_frame.items():  # itemsss
    print(key)
    # student
    # 0    Angela
    # 1     James
    # 2      Lily
    # Name: student, dtype: object
    print(value)
    # score
    # 0    56
    # 1    76
    # 2    98
    # Name: score, dtype: int64


# inbuilt pandas loop
for index, row in student_data_frame.iterrows():
    print(row)
    # Name: score, dtype: int64
    # student    Angela
    # score          56
    # Name: 0, dtype: object
    # student    James
    # score         76
    # Name: 1, dtype: object
    # student    Lily
    # score        98
    # Name: 2, dtype: object

for index, row in student_data_frame.iterrows():
    print(row.student)
    # Angela
    # James
    # Lily

for index, row in student_data_frame.iterrows():
    print(row.score)
    # 56
    # 76
    # 98

for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
        # 56
