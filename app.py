import pymongo
from classes import data, DATA, Dataprocess
from classes import Enrollments, Students, Courses,Careers
from dotenv import load_dotenv
from classes.DbMongo import DbMongo
def main():
    
    client, db = DbMongo.getDB()
    pipeline = Dataprocess(DATA)

    #collection = db.data
    #collection.insert_many(DATA)
    
   # pipeline.create_careers(db)
   # pipeline.create_students(db)
    pipeline.create_enrollments(db)

    print(db.list_collection_names())
   
    return True

if __name__ == "__main__":
    load_dotenv()
    main()
