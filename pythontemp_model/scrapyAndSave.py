import modelCragList_v2_debug
import modelkbb_v1_debug
import xmlprocess_v1
from time import sleep

def savePreviousDay():
    usercarlist=modelCragList_v2_debug.craglistsearchAll()
    xmlprocess_v1.newXml("car.xml")
    for i in range(len(usercarlist.modellist)):
        writeXml("car.xml",usercarlist.modellist[i],usercarlist.pricelist[i],usercarlist.year[i],usercarlist.carlinklist[i],usercarlist.abstracIlist[i],usercarlist.timepostlist[i])

savePreviousDay()
  
