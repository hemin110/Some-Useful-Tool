#encoding=utf-8
import os
from urllib import parse , request
import json

rootPath =u'F:/'
fileName = 'formtitle.txt'
savePath = u'E:/workgit/train-title-recognition/TextCNN/files/titlts_file'
positiveFileName = u'positive_titles_t.txt'
loujiFileName = u'louji_titles.txt'

formatList = []
positiveList = []

with open(os.path.join(rootPath,fileName) , 'r' , encoding='utf-8') as f:
    for line in f:
        formatList.append(line)

with open(os.path.join(savePath,positiveFileName) , 'r' , encoding='utf-8') as f:
    for line in f:
        positiveList.append(line)


print(len(formatList))
print(len(set(formatList)))
print(len(positiveList))


loujiList = [word for word in formatList if word not in positiveList]
print(len(loujiList))
##漏掉339个标签



##漏掉的数据统计

with open(os.path.join(savePath,loujiFileName) , 'a+' , encoding='utf-8') as wf:
    for line in set(loujiList):
        wf.write(line)




# with open(os.path.join(savePath,fileName) , 'a+' , encoding='utf-8') as wf:
#     for line in set(formatList):
#         wf.write(line)
