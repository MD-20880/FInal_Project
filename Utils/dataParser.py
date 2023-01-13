###data would be present in such format:
#           [Para , value, time]

#inside database, all the data will be stored in such format
#   key : Device_Name:Parameter    value : Value:time(in second from Jan 1, 1970, 00:00:00)


#a batch of data will be written in a single line. Each line follow pattern below
# {DEVICE_NAME};({PARAMERTER}:{VALUE};)+TIME:TIME_IN_SECOND

# e.g: Device1;Temperature:23.3234;Humidity:2.3423;Time:1673450815.48



def parseLine(line:str)->list:
    elements = line.split(";")
    deviceName = elements[0]
    elements = elements[1:]
    result = [[i.split(":")[0],i.split(":")[1]] for i in elements]
    result = [deviceName] + result
    return result     
    

def readFile(file:str)->list:
    with open(file) as f:
        data = f.readlines()
    data = [i[:-1] for i in data]
    resultdata = [parseLine(i) for i in data]
    return resultdata


