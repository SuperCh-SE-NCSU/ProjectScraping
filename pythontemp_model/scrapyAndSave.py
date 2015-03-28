import modelCragList_v3_debug
import modelkbb_v1_debug
import xmlprocess_v1
from time import sleep

def savePreviousDay():
    usercarlist=modelCragList_v3_debug.craglistsearchAll()
    xmlprocess_v1.newXml("car.xml")
    for i in range(len(usercarlist.modellist)):
        xmlprocess_v1.writeXml("car.xml",usercarlist.modellist[i],usercarlist.pricelist[i],usercarlist.year[i],usercarlist.carlinklist[i],usercarlist.abstractIlist[i],usercarlist.timepostlist[i])

savePreviousDay()
  
