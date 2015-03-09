import modelCragList_v1_debug
import modelkbb_development.py

def craglistsearchKbb(mcarlist):
    html_content='<html>'
    
    for i in range(len(mcarlist.modellist)):
        tempprice=getKbbPrice(mcarlist.make[i],mcarlist.model[i],mcarlist.year[i],mcarlist.mileage[i])
        temp_content='<p> make: '+mcarlist.make[i]+', model'+mcarlist.model[i]+', '+
