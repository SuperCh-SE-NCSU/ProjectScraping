import modelCragList_v1_debug
import modelCragList_v2_debug
from time import time
def comparetest:
    carlist={'camry','civic','accord'}
    time1=list()
    number1=list()
    time2=list()
    number2=list()
    for i in carlist:
        t1=time()
        usercarlist1=modelCragList_v1_debug.craglistsearch('toyota','camry','2007','2010',5000,10000,'2015-03-27 23:40:13')
        t2=time()
        time1.append(t2-t1)
        number1.append(len(usercarlist1.pricelist))
        t1=time()
        usercarlist1=modelCragList_v2_debug.craglistsearch('toyota','camry','2007','2010',5000,10000,'2015-03-27 23:40:13')
        t2=time()
        time2.append(t2-t1)
        number2.append(len(usercarlist1.pricelist))
