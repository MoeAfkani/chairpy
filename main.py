#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import chairPy as cp
import pickle 

stdList = [] #Students List
tchrList= [] #Teachers List
crsList = [] #Courses  List

"""   Read Files to Obj    """
for l in cp.excel('Test.xlsx'):
    stdList.append(cp.Student(l[0],l[1],l[2]))




"""   Read Files to Obj    """


"""   Save Obj to files    """
stdFile  = open('data/stdFile.obj' , 'wb')
tchrList = open('data/tchrList.obj', 'wb')
crsList  = open('data/crsList.obj' , 'wb')

for s in stdList:
    pickle.dump(s, stdFile)