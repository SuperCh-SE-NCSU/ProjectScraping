import modelCragList_v1_debug
import modelCragList_v2_debug
from time import time
import datetime
#sudo apt-get build-dep python-matplotlib
import numpy as np  

class carmodelge():
    def __init__(self,carmodel,carmake):
        self.carmake=carmake
        self.carmodel=carmodel


    
def comparetest(day):
    previoustime=(datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    test1=carmodelge('camry','toyota')
    test2=carmodelge('corolla','toyota')
    test3=carmodelge('accord','honda')
    test4=carmodelge('civic','honda')
    testlist=list()
    testlist.append(test1)
    testlist.append(test2)
    testlist.append(test3)
    testlist.append(test4)
    time1=list()
    number1=list()
    time2=list()
    number2=list()
    for i in range(len(testlist)):
        t1=time()
        usercarlist1=modelCragList_v1_debug.craglistsearch(testlist[i].carmake,testlist[i].carmodel,'2007','2010',1000,12000,previoustime)
        t2=time()
        time1.append(t2-t1)
        number1.append(len(usercarlist1.pricelist))
        t1=time()
        usercarlist2=modelCragList_v2_debug.craglistsearch(testlist[i].carmake,testlist[i].carmodel,'2007','2010',1000,12000,previoustime)
        t2=time()
        time2.append(t2-t1)
        number2.append(len(usercarlist2.pricelist))
        print usercarlist1.abstractIlist
        print usercarlist2.abstractIlist
        #time.sleep(10)
    print number1
    print number2
    print time1
    print time2
    
comparetest(1)
#A={1,2,3,4}
#B={2,1,4,3}
#print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
#print (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
#[6, 0, 4, 4]
#[10, 2, 9, 8]
#[32.72494292259216, 26.515918016433716, 27.903974056243896, 24.822060108184814]
#[53.5358350276947, 48.663240909576416, 57.4665470123291, 51.33353900909424]

#[4, 2, 2, 1]
#[4, 2, 2, 1]
#5,2,2
#[11.352260112762451, 7.856437921524048, 43.17771887779236, 8.285339117050171]
#[16.72474503517151, 14.028115034103394, 53.29979920387268, 18.483553171157837]
#9.05211806297,7.70969510078,59.5880839825(19.7910189629),11.4580149651

