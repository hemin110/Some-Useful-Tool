#encoding=utf-8

import os


rootPath = "F:\文本训练数据"
fileNames = ["吉林标题1.txt","吉林标题2.txt","吉林标题3.txt"]

list1 = []
list2 = []
list3 = []
listall = []
#open 1
with open(rootPath+"/"+fileNames[0] , 'r' , encoding="utf-8") as f1:
    for line in f1:
        list1.append(line.replace('\n' , ''))

print(len(set(list1)))


#open 2
with open(rootPath+"/"+fileNames[1] , 'r' , encoding="utf-8") as f1:
    for line in f1:
        list2.append(line.replace('\n' , ''))

print(len(set(list2)))



#open 3
with open(rootPath+"/"+fileNames[2] , 'r' , encoding="utf-8") as f1:
    for line in f1:
        list3.append(line.replace('\n' , ''))

print(len(set(list3)))


for line in list1:
    listall.append(line)
for line in list2:
    listall.append(line)
for line in list3:
    listall.append(line)

print(len(listall))
print(len(set(listall)))


# 写标题到文档
# with open(rootPath+"/"+"吉林总结.txt" ,'a+' , encoding='utf-8') as fw:
# #     for line in listall:
# #         fw.write(line+"\n")


# 与之前的对比
with open(rootPath+'/'+'positive_titles_t.txt' , 'r' , encoding='utf-8') as f:
    for line in f:
        listall.append(line.replace("\n",""))
print(len(listall))
print(len(set(listall)))


with open(rootPath+'/'+'err.txt' , 'r' , encoding='utf-8') as f:
    for line in f:
        listall.append(line.replace("\n",""))
print(len(listall))
print(len(set(listall)))

# 写标题到文档
with open(rootPath+"/"+"positive.txt" ,'a+' , encoding='utf-8') as fw:
    for line in listall:
        fw.write(line+"\n")