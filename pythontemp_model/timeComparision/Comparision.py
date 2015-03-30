import modelCragList_v1_debug
import modelCragList_v2_debug
from time import time
import numpy as np  
import matplotlib.pyplot as plt  
class carmodelge():
    def __init__(self,carmodel,carmake):
        self.carmake=carmake
        self.carmodel=carmodel

def showdata(A,B):  
    n_groups = 4  
    means_men =(0.9,0.9,0.73,0.67)  
    means_women = (0.77,0.87,0.77,0.73)  
    
    fig, ax = plt.subplots()  
    index = np.arange(n_groups)  
    bar_width = 0.2  
   
    opacity = 0.8  
    rects1 = plt.bar(0.8+index, means_men, bar_width,alpha=opacity, color='b',label='Forwards')  
    rects2 = plt.bar(0.8+index + bar_width, means_women, bar_width,alpha=opacity,color='r',label='Backwards')  
   
    plt.xlabel('Group')  
    plt.ylabel('Time')  
    plt.title('Mean Accuracy by Mode and Direction of questioning')  
    plt.xticks(0.8+index + bar_width, ('SeqTPL', 'CircumTPL','SeqTPL','CircumVPL'))  
    plt.xlim(0,5)
    plt.ylim(0,1)  
    plt.legend()  
   
    plt.tight_layout()  
    plt.show()
    
def comparetest():
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
        usercarlist1=modelCragList_v1_debug.craglistsearch(testlist[i].carmake,testlist[i].carmodel,'2007','2010',5000,10000,'2015-03-27 23:40:13')
        t2=time()
        time1.append(t2-t1)
        number1.append(len(usercarlist1.pricelist))
        t1=time()
        usercarlist1=modelCragList_v2_debug.craglistsearch(testlist[i].carmake,testlist[i].carmodel,'2007','2010',5000,10000,'2015-03-27 23:40:13')
        t2=time()
        time2.append(t2-t1)
        number2.append(len(usercarlist1.pricelist))
        time.sleep(30)
    print number1
    print number2
    print time1
    print time2
comparetest()
    
