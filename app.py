import pymongo
from classes import DbMongo
from classes import data, DATA, Dataprocess
from classes import *
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    pipeline = Dataprocess(data)
    #collection = db.data
    #collection.insert_many(DATA)
   # enrollments = Enrollments(db)
    #print(enrollments)
   
    pipeline.create_careers(db)
    pipeline.create_students()
    pipeline.create_enrollments(db)

    #print(DATA[2])
    return True

if __name__ == "__main__":
    load_dotenv()
    main()