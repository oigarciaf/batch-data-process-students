from classes import DbMongo
from classes.data import DATA
from classes import Enrollments
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self,db):
        ## Do something to create careers on your mongodb collection using __data
        self.__collection = "careers"
        collection = db[self.__collection]     
        
        for student in self.__data:      
            career = student['carrera']
            if not collection.find_one({'name':career}):
                collection.insert_one({'name':career})

       
        return True
    def create_courses(self,db):
        ## Do something to create courses on your mongodb collection using __data
        self.__collection = "courses"
        collection = db[self.__collection]   

        for student in self.__data:
            for course in student['cursos_aprobados'] + student['cursos_reprobados']:
                if not collection.courses.find_one({'name':course}):
                    collection.courses.insert_one({'name':course})

        return True
    def create_students(self,db):
        ## Do something to create students on your mongodb collection using __data
        self.__collection = "students"
        collection = db[self.__collection]  

        for student in self.__data:
            student_data = {
            'number_acount':student['numero_cuenta'],
            'name': student['nombre_completo'],
            'age':student['edad'],
            'career':student['carrera'],
            'approved_courses':student['cursos_aprobados'],
            'failed_courses':student['cursos_reprobados']
        }
        collection.insert_one(student_data)
        return True
    
    def create_enrollments(self, db):
        ## Do something to create enrollments on your mongodb collection using __data
        self.__collection = "enrollments"
        collection = db[self.__collection] 

        for student in self.__data:
            student_id = collection.students.find_one({'name':student['nombre_completo']},{'_id':0})
            for course in student['cursos_aprobados']:
                course_id = collection.courses.find_one({'name': course},{'_id':0})
                enrollments_data = {
                    'student_id': student_id,
                    'course_id': course_id,
                    'status': 'approved'
                }
                collection.insert_one(enrollments_data)

            for course in student['cursos_reprobados']:
                course_id = collection.courses.find_one({'name': course},{'_id':0})
                enrollment_data = {
                    'student_id': student_id,
                    'course_id': course_id,
                    'status': 'failed'
                }
                collection.insert_one(enrollment_data)

        return True