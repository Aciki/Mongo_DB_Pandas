import pymongo
import numpy as np
from bson import json_util
import json
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
from datetime import datetime


class Database:
    dbName="restoran"
    
    def __init__(self,pymongo):
        self.conection = pymongo.MongoClient("mongodb://localhost:27017/")
        
   

    def find_return(self, collectionName):
        myDB=self.conection[self.dbName]
        myCol=myDB[collectionName]
        return myCol
        
            


class ModelCompanies(Database):
    collectionName = "data"

    def __init__(self, pymongo):
        Database.__init__(self, pymongo)
    
    def colection(self):
        return Database.find_return(self, self.collectionName)

        
        
object11 = ModelCompanies(pymongo)
x = object11.colection()
df = pd.DataFrame(list(x.find()))
df = df[pd.notnull(df['promocija'])]
try:
    for a in x.find():
        b= (a["datum"])
        a = b.strftime('%m/%d/%Y')
        df.append([b])
except AttributeError:
    pass
df = df.dropna(how='all', axis=1)


print(df)
v = df.groupby(['den']).mean()
print(v)



fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['datum'],
     df['promet'],
     color='red')

ax.set(xlabel="datum",
       ylabel="promet ",
       title=" Meze Bar, promet 2019 juli avgust")

plt.show()
print(df.describe())
