'''
Bryant Le
m02_lab.py
This program will determine if a student's GPA will qualify them on the Dean's List or the Honor Roll
'''

dean_number = 3.5
honor_number = 3.2

student_last = input(
    "What is the student's last name? Please enter 'ZZZ' to quit: ")

while student_last != 'ZZZ':
    student_first = input("Please enter the student's first name: ")
    student_gpa = float(input("Please enter the student's GPA: "))
    if student_gpa >= dean_number:
        print("Student is on the Dean's List.")
    elif student_gpa >= honor_number:
        print("Student is on the Honor Roll.")
    else:
        print("Student does not qualify for Dean's List and Honor Roll.")
    student_last = input(
        "What is the student's last name? Please enter 'ZZZ' to quit: ")

print("Thank you for using this program. Goodbye.")
