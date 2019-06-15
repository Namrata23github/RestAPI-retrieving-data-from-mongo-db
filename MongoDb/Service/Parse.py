import json

from Repository.CallApi import getData


def parseIt(securityId):
    mapOfData = getData(securityId);
    list =[]
    mapOfNonData =[]
    for i in mapOfData:
        if str(i['v'])[:1] != '_':
            mapOfNonData.append(i)
    for i in mapOfNonData:
        jsonValue = json.dumps(str(i))
        list.append(json.loads(jsonValue))
    return list

