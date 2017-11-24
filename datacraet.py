#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 07:51:46 2017

@author: hemin
"""
import os
import time
import pandas as pd
import numpy as np


test_path = u"/media/hemin/LENOVO/数据/火电厂/2016年2月中控数据/70HAD20CT203.txt"

begin_data = "2017/11/5 0:00:00"
end_data = "2017/11/15 0:00:00"


def timeChange(tempdata):
    timearray = time.strptime(tempdata , "%Y/%m/%d %H:%M:%S")
    time_simple = time.mktime(timearray)
    return time_simple

def createData(test_path, begin_data, end_data):
    filename = test_path.split("/")[-1].replace(".txt", "")
    f = open(test_path)
    temp_num = f.readlines(1)[0].split("\t")[1]
    print (temp_num)
    if temp_num == 'System.__ComObject\n':
        temp_num = 0
    else:
        temp_num = float(f.readlines(1)[1].split("\t")[1])
    dic = {}

    b_time = timeChange(begin_data)
    e_time = timeChange(end_data)

    for i in range(int(b_time) , int(e_time+1)):
        #time_local = time.localtime(i)
        #dt = time.strftime("%Y/%m/%d %H:%M:%S", time_local)
        dic[i] = -100

    for line in f.readlines():
        if line!="\n":
            t , v = line.split("\t")
            if v == 'System.__ComObject\n':
                v=-100
            t_new = int(timeChange(t))
            if t_new in dic:
                dic[t_new] = v
                #temp_num = float(dic[t_new])
    new_file = open(filename , "w")
    for i in range(int(b_time), int(e_time)):
        if dic[i] == -100:
            new_file.write(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(i))+"\t"+str(dic[i])+"\n")
        else:
            new_file.write(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(i)) + "\t" + (dic[i]))
    new_file.close()

    data_table = pd.read_table(filename,header=None)
    data = np.asanyarray(data_table)

    [row, col] = data.shape
    for i in range(row):
        if i == 0:
            if data[i, 1]==-100:
                data[i, 1] = temp_num
        else:
            if data[i, 1]==-100:
                data[i, 1] = data[i - 1, 1]
    data = data[1::60,:]
    df = pd.DataFrame(data)
    os.remove(filename)
    df.to_csv("data/"+filename+".csv" , header=None , index=False)
    # content = []
    # for line in f.readlines():
    #     content.append(line)
    #
    # for i in range(len(content)):
    #     if content[]



data_path = u"/media/hemin/LENOVO/数据/火电厂/点火11月1日到11月18日数据-11号并网/"
f_dir = os.listdir(data_path)
for f_name in f_dir:
    print (f_name)
    createData(data_path+f_name, begin_data, end_data)