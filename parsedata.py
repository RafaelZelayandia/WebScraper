import json
with open("tweets.json") as json_data:
    jsonData = json.load(json_data)
for i in jsonData:
    print (i)
'''for i in jsonData:
    if "obama" in i['tweet'].lower():
        print (i)
'''
