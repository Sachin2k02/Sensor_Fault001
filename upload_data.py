from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://Sachin:Sachin@cluster0.meu0tjf.mongodb.net/?retryWrites=true&w=majority"

#create a new client and create to server

client = MongoClient(uri)

#create a database name and collection name
DATABASE_NAME = "Sachih"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("C:\Users\Admin\Desktop\ML_Projects\Sensor_Fault\notebooks\wafer_23012020_041211.csv")


df = df.drop("Unnamed: 0",axis = 1)


json_record = list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)