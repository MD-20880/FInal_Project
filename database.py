import redis



#


def build_redis_connection(host:str, port:int, db:int):
    return redis.Redis(host='localhost', port=6379, db=0)



db = build_redis_connection('localhost', 6379, 0)


def testGenerateConteents(db:redis.Redis):
    import time
    import random
    #Generate Two Devices
    
    devices = ["Device1", "Device2"]
    startTime = time.time()
    
    while time.time() < startTime+10:
        device = devices[random.randint(0,1)]
        info = random.random()*100
        currentTime = time.time()
        
        db.rpush(device+":"+"Temperature", str(info)+":"+str(currentTime))

# testGenerateConteents(db)


def getTestData()->list:
    
    db = build_redis_connection('localhost', 6379, 0)
    info1 =db.lrange("Device1:Temperature", 0, -1)
    info2 = db.lrange("Device2:Temperature", 0, -1)
    return [info1, info2]

# data = getTestData()
# print (data[0])
# print (data[1])