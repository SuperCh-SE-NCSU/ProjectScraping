import xml.etree.ElementTree as ET

def writeXml(filename,tempmake,tempmodel,tempyear,tempusername,tempcurrentTime,tempemail):
    tree=ET.parse(filename)
    root = tree.getroot()
    user=ET.Element("user",username=tempusername,make=tempmake,model=tempmodel,year=tempyear,currentTime=tempcurrentTime,email=tempemail)
    root.append(user)
    tree.write(filename)
    
def readXml(filename,makelist,modellist,yearlist,usernamelist,currentTimelist,emaillist):
    tree=ET.parse(filename)
    root=tree.getroot()
    for child in root.findall("user"):
        makelist.append(child.attrib['make'])
        modellist.append(child.attrib['model'])
        yearlist.append(child.attrib['year'])
        usernamelist.append(child.attrib['username'])
        currentTimelist.append(child.attrib['currentTime'])
        emaillist.append(child.attrib['email'])
    print len(makelist)
    
def testXml():
    writeXml("users.xml","honda","camry","2011","ldong","2015-02-18 22:57:35","dragonfly90@163.com")
    makelist=list()
    modellist=list()
    yearlist=list()
    usernamelist=list()
    currentTimelist=list()
    emaillist=list()
    readXml("users.xml",makelist,modellist,yearlist,usernamelist,currentTimelist,emaillist)
    for i in range(len(makelist)):
        print makelist[i],modellist[i],yearlist[i],usernamelist[i],currentTimelist[i],emaillist[i]

#testXml()
