import modelCragList_v2_debug
import modelkbb_v1_debug

def generateHTML(cmake_temp,cmodel_temp,cstartyear,cendyear,cminprice,cmaxprice,ctime):
    #print cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime
    cmake=cmake_temp.lower()
    cmodel=cmodel_temp.lower()
    usercarlist=modelCragList_v2_debug.craglistsearch(cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime)
    print 'user: '
    print len(usercarlist.carlinklist)
    html_content='<html>'
    temp_content='<body><center><p> Your desired car model: '+cmodel+'</p>'
    html_content=html_content+temp_content
    for i in range(len(usercarlist.modellist)):
        html_content+='<p>========================================</p>'
        html_content+='<p>'+usercarlist.abstractIlist[i]+'&nbsp;&nbsp'+usercarlist.timepostlist[i]+'</p>'
        tempprice=modelkbb_v1_debug.getKbbPrice(cmake,usercarlist.modellist[i],usercarlist.year[i],usercarlist.mileagel[i])
        temp_content='<p> year:'+usercarlist.year[i]+' &nbsp; mileage: '+usercarlist.mileagel[i]+' &nbsp;  price: '+usercarlist.pricelist[i]+'</p>'
        html_content=html_content+temp_content
        temp_content='<p> <a href=http://raleigh.craigslist.org'+usercarlist.carlinklist[i]+'>http://raleigh.craigslist.org'+usercarlist.carlinklist[i]+'</a></p>'
        html_content=html_content+temp_content
        html_content+='<table border="1" style="width:100%">'
        html_content+='<tr><td>Type</td><td>Fair</td><td>Good</td><td>Very Good</td><td>Excellent</td><td>Retail</td>'
        for key1,value1 in tempprice.iteritems():
            html_content+='<tr>'
            html_content+='<td>'+str(key1)+'</td>'
            for j in range(len(value1)):
                html_content+='<td>'+str(value1[j])+'</td>'
            html_content+='</tr>'
        html_content+='</table>'
        html_content+='<p>========================================</p>'
    html_content+='</center><body>'
    
    #Html_file= open("current.html","w")
    #Html_file.write(html_content)
    #Html_file.close()
    return html_content

def generateHTMLnoKBB(cmake_temp,cmodel_temp,cstartyear,cendyear,cminprice,cmaxprice,ctime):
    #print cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime
    cmake=cmake_temp.lower()
    cmodel=cmodel_temp.lower()
    usercarlist=modelCragList_v2_debug.craglistsearch(cmake,cmodel,cstartyear,cendyear,cminprice,cmaxprice,ctime)
    print 'user: '
    print len(usercarlist.carlinklist)
    html_content='<html>'
    html_content+='<body><p>Welcome to choose ProjectScraping Service. We will send you email with candidate car with kbb price every day. Below is the car posted no later than 24 hours</p>' 
    temp_content='<center><p> Your desired car model: '+cmodel+'</p>'
    html_content=html_content+temp_content
    for i in range(len(usercarlist.modellist)):
        html_content+='<p>========================================</p>'
        html_content+='<p>'+usercarlist.abstractIlist[i]+'&nbsp;&nbsp'+usercarlist.timepostlist[i]+'</p>'
        #tempprice=modelkbb_v1_debug.getKbbPrice(cmake,usercarlist.modellist[i],usercarlist.year[i],usercarlist.mileagel[i])
        temp_content='<p> year:'+usercarlist.year[i]+' &nbsp; mileage: '+usercarlist.mileagel[i]+' &nbsp;  price: '+usercarlist.pricelist[i]+'</p>'
        html_content=html_content+temp_content
        temp_content='<p> <a href=http://raleigh.craigslist.org'+usercarlist.carlinklist[i]+'>http://raleigh.craigslist.org'+usercarlist.carlinklist[i]+'</a></p>'
        html_content=html_content+temp_content
        html_content+='<p>========================================</p>'
    html_content+='</center><body>'
    
    #Html_file= open("current.html","w")
    #Html_file.write(html_content)
    #Html_file.close()
    return html_content

def testHTML():
    generateHTML('toyota','camry','2007','2010',5000,10000,'2015-03-06 23:40:13')


#testHTML()
    
