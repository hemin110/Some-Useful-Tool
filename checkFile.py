# encoding=utf8
import os
from urllib import parse , request
import json


success = 0
falied = 0

url = 'http://172.16.2.149:8087/recognition/recog?text='
rootPath =u'F:/'
#fileNames = ['positive_titles.txt','negative_titles.txt']
fileNames = ['formtitle.txt']

for fileName in fileNames:
    with open(os.path.join(rootPath, fileName), 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n','')
            key = request.quote(line)
            req = request.Request(url+key)
            res = request.urlopen(req)
            res = res.read()

            rJson = json.loads(res)
            if 'true' in rJson['result'] and fileName == 'positive_titles.txt':
                success=success+1
                print('success:{}',success)
            elif 'false' in rJson['result'] and fileName == 'negative_titles.txt':
                success=success+1
                print('success:{}', success)
            elif 'true' in rJson['result'] and fileName == 'formtitle.txt':
                # print(rJson)
                success = success + 1
                # print('success:', success)
            else:
                print (rJson)
                falied=falied+1
                print('falied:', falied)

