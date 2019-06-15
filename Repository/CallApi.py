import requests
import json

def getData(securityId):
    responses = callTheApi(securityId)['data'];
    k2= None
    for (k, v) in responses.items():
        # print("Key: " + str(k))
        # print("Value: " + str(v))
        for k1 in v:
           k2=json.dumps(k1['c'])
    return json.loads(k2)




def callTheApi(securityId):
    api_url = '<api>'.format(securityId)
    header = {'a': 'avalue', 'b':'bvalue', 'c': 'cvalue'}

    response = requests.get(api_url, headers=header)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))



