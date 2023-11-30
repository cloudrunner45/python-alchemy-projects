from db_creation import *
from crud_functions import *


def create_user():
    
    while True:
        user_input = input(" choose a action: \n(1) create new student\n (2) create teacher\n (e) exit\n")

        match user_input:
            case "1":
                # inputs for insert_into_student
                name = input("name: ")
                age = int(input("age: "))   
                grade = int(input("grade: "))

                insert_into_student(name, age, grade) 
                break
            case "2":
                # inputs for insert_into_teacher
                name = input("name: ")
                grade_teach = input("grade: ")

                insert_into_teacher(name, grade_teach)
                break

            case "e":
                break
            case _: 
                print("Invalid choice, please try again.")


def delete_user():
        
    while True:
        user_input = input("choose a action: \n(1) delete student\n (2) delete teacher\n (e) exit\n")

        match user_input:
            case "1":
                print_all_students()
                student_id = int(input("provide student id to be deleted: "))
                delete_student(student_id)
                break

            case "2":
                print_all_teachers()
                teacher_id = int(input("provide teacher id to be deleted: "))
                delete_teacher(teacher_id)
                break

            case "e":
                break
            case _:
                print("Invalid choice, please try again.")

def update_user():

    while True:
        user_input = input("choose a action: \n(1) update student class\n (2) update teacher class\n (e) exit\n")

        match user_input:
            case "1":
                print_all_students()
                student_id = int(input("provide student id to be updated: "))
                new_student_grade = int(input("provide new grade: "))
                update_student_grade(student_id, new_student_grade)
                break
            
            case "2":
                print_all_teachers() 
                teacher_id = int(input("provide teacher id to be updated: "))
                new_teacher_grade = int(input("provide new grade: "))
                update_teacher_grade(teacher_id, new_teacher_grade)
                break

            case "e":
                break           
            case _:
                print("Invalid choice, please try again.")

def read_users():

    while True:
        user_input = input("choose a action: \n(1) view students \n (2) view teachers \n (e) exit\n")

        match user_input:
            case "1":
                print_all_students()
                break
            case "2":
                print_all_teachers()
                break

            case "e":
                break           
            case _:
                print("Invalid choice, please try again.")           