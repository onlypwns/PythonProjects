student_1 = {'name': 'john', 'age':'22', 'grade':'B'}
student_2 = {'name': 'david', 'age':'55', 'grade':'A'}
student_3 = {'name': 'mark', 'age':'25', 'grade':'C'}
while True:
    user_input = input('What do you want to do?\n1) See all the student information\n2) Modify their grade\n3) Exit\n')
    if user_input == '1':
        print('Student1 name: ' + student_1['name'].capitalize() + ', age: ' + student_1['age'] + ', grade: ' + student_1['grade'])
        print('Student2 name: ' + student_2['name'].capitalize() + ', age: ' + student_2['age'] + ', grade: ' + student_2['grade'])
        print('Student3 name: ' + student_3['name'].capitalize() + ', age: ' + student_3['age'] + ', grade: ' + student_3['grade'])
    elif user_input == '2':
        input_grade = input("Which student's grade you want to modify? (1, 2, or 3)\n")
        if input_grade == '1':
            # current grade check
            print('The current grade of the student is ' + student_1['grade'].capitalize())
            # modify the value of the grade for student1
            new_grade = input('What is the new grade for the student?\n')
            student_1['grade'] = new_grade
            print(f"The student's new grade is {new_grade.capitalize()}")
        elif input_grade == '2':
            # current grade
            print('The current grade of the student is ' + student_2['grade'].capitalize())
            new_grade = input('What is the new grade for the student?\n')
            # modify the value of the grade for student2
            student_2['grade'] = new_grade
            print(f"The student's new grade is {new_grade.capitalize()}")
        elif input_grade == '3':
            # current grade
            print('The current grade of the student is ' + student_3['grade'].capitalize())
            new_grade = input('What is the new grade for the student?\n')
            # modify the value of the grade for student3
            student_3['grade'] = new_grade
            print(student_3['grade'])
            print(f"The student's new grade is {new_grade.capitalize()}")
    else:
        break




