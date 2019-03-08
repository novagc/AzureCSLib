import AzureCSLib as az
import cognitive_face as cf
def GetParams():
    import json
    with open('faceapi.json') as jsonFile:
        key = json.load(jsonFile)['key']
    with open('faceapi.json') as jsonFile:
        group = json.load(jsonFile)['groupId']
    with open('faceapi.json') as jsonFile:
        baseURL = json.load(jsonFile)['serviceUrl']
    return az.FaceAPIsession(key, baseURL, group)
    
'''
session = GetParams()
session.GetPersonData(session.GetPersonID('0'))
session.UpdatePersonData(session.GetPersonID('0'), '123')
session.CreatePerson(data='12345')
'''
raise cf.CognitiveFaceException('400', 'GoodArg', 'abc')
