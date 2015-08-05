# -*- coding:utf8 -*-
#!usr/bin/python

####################################### PART0 Description ##############################################################

# Filename: separate_questions_and_answers.py
# Description : separate questions and matching answers from a file
# Author:ZhMi
# E-mail:zmmingtiandege1314@126.com
# Create:2015-8-3

####################################### Part1 : Coding #################################################################

AnswList = list()
QuesList = list()
TempList = list()

fp = open("/home/zhmi/Documents/eyadatabase/erya_data.ini")

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
        QuesList.append((line[:equ_sign_index]).strip())
        AnswList.append((line[equ_sign_index+1:]).strip())
        '''
        if line.find('\n') == -1 :
            AnswList.append(line[equ_sign_index+1:])
        else :
            AnswList.append(line[equ_sign_index+1:line.find('\n')])
        '''
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
            QuesList.append(TempList[0].strip())
            AnswList.append(TempList[1].strip())

            '''
            TempList[1] = (TempList[1])[:(TempList[1]).find('\n')]
            AnswList.append(TempList[1])
            '''

    map(separate_lines,LineList)

finally :
    fp.close()

######################################### Test function Part ###########################################################
'''
for i in xrange(len(AnswList)) :
    print i+1, QuesList[i]
    print AnswList[i]
'''
######################################### Create dataBase and tables Part ##############################################

import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='95120',charset='utf8',port=3306)
cursor = conn.cursor()

try :
    cursor.execute("""create database eryadb default character set utf8 collate utf8_general_ci""")

except :
    cursor.execute("use eryadb")

finally :
    pass

try :
    cursor.execute("create table QuesTotalTable(id int auto_increment primary key,question varchar(400),answer varchar(100))engine = innodb default charset = utf8;")

except :
    pass

finally:
    pass

######################################## Insert local data into table Part##############################################

try :
    cursor.execute("set names utf8")
    QueAnsList = map(None,QuesList,AnswList) # combine QuesList and AnswerList .[(question[0],answer[0]),(question[1],answer[1]),...]
    '''
    [First version of inserting datas]
    for k in xrange(len(AnswList)) :
        cursor.execute('insert into QuesTotalTable(question,answer) values(%s,%s)',QueAnsList[k])
    '''

    #[Second version of inserting datas]
    def insertfun(tuple) :
        cursor.execute('insert into QuesTotalTable(question,answer) values(%s,%s)',tuple)

    map(insertfun,QueAnsList)
    conn.commit()

except MySQLdb.Error,e :
    print "Wrong Operations on MySQL."

finally :
    pass

######################################## Create view of determine-question Part#########################################

try :
    #cursor.execute("""create view DetQueView as select * from QuesTotalTable where answer like "是_" or answer like "否_" or answer like "是__"; """)
    cursor.execute("""create view DetQueView as select * from QuesTotalTable where answer = "是" or answer = "否" or answer like "是_"; """)
    conn.commit()

except :
    pass

finally:
    pass

######################################## Create view of selectse-question and fill-blank-question Part##################

try :
    cursor.execute("""create view SelFilView as select * from QuesTotalTable where id not in(select id from DetQueView); """)

except :
    pass

finally:
    cursor.close()
    conn.close()

#import re
#AnswList = map(lambda answer: re.compile("(.*)\n").findall(answer), AnswList)
#AnswList = sum(map(lambda answer: answer[:answer.find('\n')], AnswList), [])











