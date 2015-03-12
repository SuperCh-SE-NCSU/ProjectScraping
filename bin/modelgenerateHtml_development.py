import modelCragList_v1_debug
import modelkbb_v1_debug

def generateHTML(cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime):
    print cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime
    usercarlist=modelCragList_v1_debug.craglistsearch(cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime)
    print len(usercarlist.carlinklist)
    html_content='<html>'
    temp_content='<body><center><p> model: '+cmodel+'</p>'
    html_content=html_content+temp_content
    for i in range(len(usercarlist.modellist)):
        tempprice=modelkbb_v1_debug.getKbbPrice(cmake,usercarlist.modellist[i],usercarlist.year[i],usercarlist.mileagel[i])
        temp_content='<p> year: '+usercarlist.year[i]+' mileage: '+usercarlist.mileagel[i]+'</p>'
        html_content=html_content+temp_content
        temp_content='<p> <a href=http://raleigh.craigslist.org'+usercarlist.carlinklist[i]+' target="_blank">http://raleigh.craigslist.org'+usercarlist.carlinklist[i]+'</a></p><p>'+usercarlist.abstractIlist[i]+'</p>'
        html_content=html_content+temp_content
        for key1,value1 in tempprice.iteritems():
            temp_content='<p> style: '+str(key1)+'</p><p>'+str(value1)+'</p>'
            html_content=html_content+temp_content
        html_content+='<p>========================================</p></center><body>'
    return html_content
    #Html_file= open("current.html","w")
    #Html_file.write(html_content)
    #Html_file.close()

def testHTML():
    generateHTML('toyota','camry','2007','2010',5000,10000,'2015-03-06 23:40:13')

#testHTML()
    
