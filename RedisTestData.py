import redis
import database.database as database
import Utils.dataParser as dataParser
import datetime
from pprint import pprint






def logParameter(device:str, data:list, time:str,  db:redis.Redis)->None:
    key = device + ":" + (data[0].upper())
    value = data[1] + ":" + time
    db.lpush(key,value)
    
        
def logBatch(batch:list, db:redis.Redis)->None:
    device = batch[0]
    time = batch[-1][1]
    dataList = batch[1:-1]
    for data in dataList:
        logParameter(device,data,time,db)
        
def logData(data:list, db:redis.Redis)->None:
    for batch in data:
        logBatch(batch,db)


# data = dataParser.readFile('/Users/mac/COMS/Final_Project/Utils/testdata')


#receive Rawdata received by readList, parse and seperate it into [value:list , time:list]
def rawToTime(rawdata)->list:
    value = []
    timeLine = []
    for data in rawdata:
        elements = str(data).split(":")
        value.append(elements[0])
        print(elements)
        timeLine.append(datetime.datetime.fromtimestamp(float(elements[1])))
    return [value,timeLine]
    
    

#TODO Read Data From Database and parse it into usable data structure.
def readList(key:str, db:redis.Redis) -> list:
    rawdata = []
    if db.exists(key):
        rawdata = db.lrange(key,0,-1)
       
    return rawdata
    




if __name__ == "__main__":
    pass
    
    
    
    



