import pymongo
from classes import DbMongo
from classes import data, DATA, Dataprocess
from classes import Enrollments, Students, Courses,Careers
from dotenv import load_dotenv

def main():

    client, db = DbMongo.getDB()
    pipeline = Dataprocess(data)

    collection = db.data
    collection.insert_many(DATA)
   
   
    pipeline.create_careers(db)
    pipeline.create_students(db)
    pipeline.create_enrollments(db)

    
   
    return True

if __name__ == "__main__":
    load_dotenv()
    main()