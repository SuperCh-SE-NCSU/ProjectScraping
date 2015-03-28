import xml.etree.ElementTree as ET

def newXml(filename):
    root=ET.Element("cars")
    tree=ET.ElementTree(root)
    tree.write(filename)
    
def writeXml(filename,tempmodel,tempprice,tempyear,tempcarlink,tempabstractInf,temptimePost):
    tree=ET.parse(filename)
    root = tree.getroot()
    carIn=ET.Element("car",model=tempmodel,price=tempprice,year=tempyear,carlink=tempcarlink,abstractInf=tempabstractInf,timePost=temptimePost)
    root.append(carIn)
    tree.write(filename)
    
def readXml(filename,modellist,pricelist,yearlist,carlinklist,abstractInflist,timePostlist):
    tree=ET.parse(filename)
    root=tree.getroot()
    for child in root.findall("car"):
        modellist.append(child.attrib['model'])
        pricelist.append(child.attrib['price'])
        yearlist.append(child.attrib['year'])
        carlinklist.append(child.attrib['carlink'])
        abstractInflist.append(child.attrib['abstractInf'])
        timePostlist.append(child.attrib['timePost'])
    print len(modellist)
    
def testXml():
    newXml("car.xml")
    writeXml("car.xml","camry","9000","2011","link","Good car","2015-02-18 22:57:35")

    modellist=list()
    pricelist=list()
    yearlist=list()
    carlinklist=list()
    abstractInflist=list()
    timePostlist=list()
    
    readXml("car.xml",modellist,pricelist,yearlist,carlinklist,abstractInflist,timePostlist)
    for i in range(len(modellist)):
        print modellist[i],pricelist[i],yearlist[i],carlinklist[i],abstractInflist[i],timePostlist[i]

#testXml()
