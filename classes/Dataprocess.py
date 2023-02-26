from classes import DbMongo
from classes import DATA, Dataprocess
from classes import Enrollments
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self,db):
        ## Do something to create careers on your mongodb collection using __data
        # Se crea una lista de carreras
        careers = list(set([d['carrera'] for d in self.__data]))
    
        # Se inserta cada carrera en la colección de carreras
        for c in careers:
             db.careers.insert_one({'name': c})
        return True
    def create_courses(self,db):
        # Se crea una lista de cursos
        courses = []
        for d in self.__data:
            for c in d['cursos_aprobados'] + d['cursos_reprobados']:
                courses.append(c)
        courses = list(set(courses))
        
        # Se inserta cada curso en la colección de cursos
        for c in courses:
            db.courses.insert_one({'name': c})
        ## Do something to create courses on your mongodb collection using __data
        return True
    def create_students(self,db):
        ## Do something to create students on your mongodb collection using __data
        # Se inserta cada estudiante en la colección de estudiantes
        for d in self.__data:
            db.students.insert_one({
                'name': d['nombre_completo'],
                'age': d['edad'],
                'career': d['carrera']
            })
        return True
    def create_enrollments(self, db):
        ## Do something to create enrollments on your mongodb collection using __data
    # Se inserta cada rejistro en la colección de inscripcion
        for d in self.__data:
            student_id = db.students.find_one({'name': d['nombre_completo']})['_id']
            for course in d['cursos_aprobados']:
                course_id = db.courses.find_one({'name': course})['_id']
                db.enrollments.insert_one(Enrollments(student_id, course_id, True).to_dict())
            for course in d['cursos_reprobados']:
                course_id = db.courses.find_one({'name': course})['_id']
                db.enrollments.insert_one(Enrollments(student_id, course_id, False).to_dict())
    
        return True