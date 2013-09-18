#!/usr/bin/env python
"""@author: Aadesh Neupane
    Simplest implementation of KNN algorithm using euclidean Algorithm
    Data set used is Eris data set and same data set is used for testing
    Using K=3
"""

import math
import os

#Calculated the euclidean distance
def euclidean(v1,v2):
	d=0.0
	for i in range(len(v1)):
		d+=(v1[i]-v2[i])**2
	return math.sqrt(d)

def getdistances(data,vec1):
    distancelist=[]
    for i in range(len(data)):
        vec2=data[i]['input']
        distancelist.append((euclidean(vec1,vec2),i))
    distancelist.sort( )
    return distancelist

def knnestimate(data,vec1,k=3):
    # Get sorted distances
    dlist=getdistances(data,vec1)
    #print dlist
    avg=0.0
    # Take the average of the top k results
    for i in range(k):
        idx=dlist[i][1]
        #print idx
        #print data[idx]['result']
        avg+=data[idx]['result']
        #print avg
    avg=avg/k
    return avg

def getTestDataSet():
    rows=[]
    sto=0
    if os.path.isfile('test.data'):
        a=open('test.data','r')
        data=a.readlines()
        for line in data:
            att=line.split(",",5)
            rows.append({'input':(float(att[0]),float(att[1]),float(att[2]),float(att[3]))})
        return rows
        #print rows
        print rows[0]['input']
    
    else:
        print "File not found\n"
        


def getIrisDataSet():
    rows=[]
    sto=0
    if os.path.isfile('iris.data'):
        a=open('iris.data','r')
        data=a.readlines()
        for line in data:
            att=line.split(",",5)
            sele=att[0]
            sewd=att[1]
            pele=att[2]
            pewd=att[3]
            res=att[4].strip()
            if res == "Iris-setosa":
                sto=1
            elif str(res)=="Iris-versicolor":
                sto=2
            elif str(res)=="Iris-virginica":
                sto=3
            else:
                print "Error"
            #print sto
            rows.append({'input':(float(sele),float(sewd),float(pele),float(pewd)),'result':sto})
        return rows
        #print rows
        #print euclidean(rows[0]['input'],rows[1]['input'])
    
    else:
        print "File not found\n"

#getIrisDataSet()
def findKNN():
    data=getTestDataSet()
    for i in range(len(data)):
        ans=knnestimate(getIrisDataSet(),data[i]['input'])
        if ans==1:    
            print "Iris-setosa"
        elif ans==2:
            print "Iris-versicolor"
        else:
            print "Iris-virginica"
            
findKNN()