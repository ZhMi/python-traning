# -*- coding : utf-8 -*-

AnswList = list()
QuesList = list()
TempList = list()

fp = open("/home/zhmi/Documents/eyadatabase/test_data_base.txt")

try :
    List = fp.readlines()
    for line in List :
        index = line.find('=')
        if index != -1 :
            QuesList.append(line[:index])
            AnswList.append(line[index+1:])

except :
    line = fp.readline()
    while line :
        TempList=line.split('=')
        if len(TempList)==2 :
            QuesList.append(TempList[0])
            AnswList.append(TempList[1])
        line = fp.readline()

finally:
    for i in AnswList :
        print i
    for j in QuesList :
        print j
    fp.close()







