from db_creation import *


# CREATE USER

#create student
def insert_into_student(name, age, grade):
    new_record = Student(name=name, age=age, grade=grade)
    session.add(new_record)
    session.commit()
    print("new student has been created successfully")

#create teacher
def insert_into_teacher(name, grade_teach):
    new_record = Teacher(name=name, grade_teach=grade_teach)
    session.add(new_record)
    session.commit()
    print("new teacher has been created successfully")


#DELETE USER

# delete student
def delete_student(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    session.delete(student)
    session.commit()
    print(f"Student with ID {student_id} deleted successfully.")

# delete teacher
def delete_teacher(teacher_id):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    session.delete(teacher)
    session.commit()
    print(f"Teacher with ID {teacher_id} deleted successfully.")

#UPDATE USERS

# update student grade 
def update_student_grade(student_id, new_student_grade):
    student = session.query(Student).filter_by(id=student_id).first()
    student.grade = new_student_grade
    session.commit()
    print(f"Student with ID {student_id} grade updated successfully.")

# update teacher grade 
def update_teacher_grade(teacher_id, new_teacher_grade):
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    teacher.grade_teach = new_teacher_grade
    session.commit()
    print(f"Teacher with ID {teacher_id} grade updated successfully.")







pass 
def get_student_query():
    x = input("Select the option for the provided results\n a - Get all students\n b - Get individual student by ID\n")
    while x != "a" and x != "b":
         input("Select the option for the provided results\n a - Get all students\n b - Get individual student by ID\n")
        
    if x == "a":
        all_students = session.query(Student).all()
        for student in all_students:
            print(f"Student ID: {student.id}, Name: {student.name}, Grade: {student.grade}")
            
    else:
        student_id = input("Provide a student ID: ")
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            print(f"Student ID: {student.id}, Name: {student.name}, Grade: {student.grade}")
        else:
            print("Student not found.")

def get_teacher_query():
    x = input("Select the option for the provided results\n a - Get all teachers\n b - Get individual teacher by ID\n")
    while x != "a" and x != "b":
        x = input("Select the option for the provided results\n a - Get all teachers\n b - Get individual teacher by ID\n")

    if x == "a":
        all_teachers = session.query(Teacher).all()
        for teacher in all_teachers:
            print(f"Teacher ID: {teacher.id}, Name: {teacher.name}, Grade Taught: {teacher.grade_teach}")
            
    else:
        teacher_id = input("Provide a teacher ID: ")
        teacher = session.query(Teacher).filter_by(id=teacher_id).first()
        if teacher:
            print(f"Teacher ID: {teacher.id}, Name: {teacher.name}, Grade Taught: {teacher.grade_teach}")
        else:
            print("Teacher not found.")
