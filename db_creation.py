#import from sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

#database connection
engine = create_engine('postgresql://joeymorgenstern:joe12@localhost/tech_track_db')
Base = declarative_base()

#model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Integer)

    def __repr__(self):
        return f"Student ID: {self.id}, Name: {self.name}, Grade: {self.grade}"

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    grade_teach = Column(Integer)
    
    def __repr__(self):
        return f"Teacher ID: {self.id}, Name: {self.name}, Grade Taught: {self.grade_teach}"

#creating the db based on above classes
Base.metadata.create_all(engine)
# create the session to interact with db
Session = sessionmaker(bind=engine)
session = Session()

# return/ students
def get_all_students():
    return(session.query(Student).all())

# print students 
def print_all_students():
    students = get_all_students()
    for student in students:
        print(student)  

# return teachers
def get_all_teachers():
    return(session.query(Teacher).all())

#print teachers
def print_all_teachers():
    teachers = get_all_teachers()
    for teacher in teachers:
        print(teacher)  



