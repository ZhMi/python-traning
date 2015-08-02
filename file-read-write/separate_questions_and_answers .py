# -*- coding : utf-8 -*-
#!usr/bin/python

####################################### PART0 DESCRIPTION ####################################

# Filename: separate_questions_and_answers.py
# Description : separate questions and matching answers from a file
# Author:ZhMi
# E-mail:zmmingtiandege1314@126.com
# Create:2015-8-3

###################################### Coding ################################################

AnswList = list()
QuesList = list()
TempList = list()

fp = open("/home/zhmi/Documents/eyadatabase/test_data_base.txt")

#[The first vison]

'''
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
'''

#[The second vison]

try :
    List = fp.readlines()

    def separate_lines(line) :
        equ_sign_index = line.find("=")
        if equ_sign_index == -1 : return
        QuesList.append(line[:equ_sign_index])
        AnswList.append(line[equ_sign_index+1:])

    map(separate_lines,List)

except :
    line = fp.readline()
    LineList=list()

    while line :
        LineList.append(line)
        line=fp.readline()

    def separate_lines(line) :
        TempList = line.split('=')
        if len(TempList) == 2 :
            QuesList.append(TempList[0])
            AnswList.append(TempList[1])

    map(separate_lines,LineList)

finally :
    fp.close()

######################################### Test Function Part ######################################

for i in xrange(len(AnswList)) :
    print i+1, QuesList[i]
    print AnswList[i]





