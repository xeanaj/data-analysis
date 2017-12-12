import json
import codecs

jsonFileName = "jtbcnews_limit_1000_2017-12-06_2016-12-08.txt"
json_data = codecs.open(jsonFileName, 'r', encoding='utf-8-sig').read()
data = json.loads(json_data.replace('\r\n', ''))


writeFileName = "jtbcnews_message_2017-12-06_2016-12-08.txt"
writeFile = open(writeFileName, "w")


def getMessage(datas) :
  for data in datas :
    writeFile.write(data["message"])
    writeFile.write('\r\n')
    
getMessage(data["posts"]["data"])
writeFile.close()

#print(data.keys())
