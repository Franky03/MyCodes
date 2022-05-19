import pandas as pd
numbers= [1,2,3]
new_list=[n+1 for n in numbers]
print(new_list)

name= 'kAIky'
letters_list= [letter for letter in name]
print(letters_list)

new_range= [r*2 for r in range(1,5)]
print(new_range)

#Conditional LC
# new_list= [ne_item for item in list if test]
names=['Alex', 'Beth','Caroline', 'Eleanor', 'Dave', 'Freddie']
short_name= [name for name in names if len(name)<5]
upper_name= [name.upper() for name in names if len(name)>=5]
print(short_name)
print(upper_name)

#DICT COMPRE
import random
students_score= {student:random.randint(1,10) for student in names}
passed_students= {student: score for (student, score) in students_score.items() if score>6}
print(passed_students)
# new_dict= {new_key: new_value for (key, value) in dict.items()if test}

student_dict={'students': ['Angela', 'James', 'Lily'], 'score': [56, 76, 98]}
# for k, v in student_dict.items():
#     print(v)

student_dataframe= pd.DataFrame(student_dict)
print(student_dataframe)
for index, row in student_dataframe.iterrows():
    if row['students'] == 'Angela':
        print(row.score)
    # print(row.score)
    # print(row.students)