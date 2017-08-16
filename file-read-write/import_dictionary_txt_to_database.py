#-*- coding:utf8 -*-
#!usr/bin/python

####################################### PART0 Description ##############################################################

# Filename:     import_dictionary_txt_to_database.py
# Description : reading a txt of chinese dictionary,and import word，meaning，source(name of source txt) into table
#               ---chinese_word_table

# Author:       ZhMi
# E-mail:      
# Create:       2015-8-18

####################################### Part1 : Import part ############################################################

import sys
import os
import string
reload(sys)
sys.setdefaultencoding("utf-8")

import MySQLdb

####################################### Part1 : Word segmentation ######################################################

fp = open("/home/zhmi/Documents/dictionary/【现代汉语词典】.txt")
TempList = fp.readlines()
fp.close()

LineList = list()

def FilterFun(line):
    line = line.decode('utf-8')
    LineList.append(line.strip())

map(FilterFun,TempList)
LineList = filter(lambda x:x!=''and (x[0]=='【' or x[0]=='*'),LineList)

wordlist = list()
meaninglist = list()

def SeprateFun(line):
    line = line.decode('utf-8')
    if line[0] == '【':
        line = line[1:]
        wordlist.append((line.split('】'))[0])
        meaninglist.append((line.split('】'))[1])
    else:
        wordlist.append(line[1:2])
        meaninglist.append(line[2:])

map(SeprateFun,LineList)
dictionist = map(None,wordlist,meaninglist)

####################################### Part2 : store to database ######################################################



conn = MySQLdb.connect(host='localhost',user='root',passwd='',charset='utf8',port=3306)
cursor = conn.cursor()

try :
    cursor.execute("use wordDB;")
    '''
    [first vison]
    for k in xrange(len(dictionist)):
        cursor.execute('insert into  chinese_word_table(word,meaning) values(%s,%s);', dictionist[k])
        conn.commit()
    '''
    '''
    [second vison]
    '''
    def InsertFun(value):
        cursor.execute('insert into  chinese_word_table(word,meaning) values(%s,%s);', value)
        conn.commit()
    map(InsertFun,dictionist)

except :
    print "Illegal Operation"
finally:
    cursor.close()
    conn.close()





