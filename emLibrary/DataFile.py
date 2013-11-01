'''
Created on 01.11.2013

@author: bernd
'''

from datetime import datetime, timedelta

class DataFile(object):
    '''
    classdocs
    '''
    
    StartDateList = []
    
    def __init__(self,DataFile):
        '''
        Constructor
        '''        
        with open(DataFile, 'rb') as content_file:
            content = content_file.read()
        temp = content.replace('\r\n', '\n').encode("hex")        
        self.dataHexList = temp[:temp.find('ffffffff')].split("e0c5ea")[1:]
        print self.dataHexList
        print self.getdec(2,2,self.dataHexList[0])
        self.parse()

    def getinfoHex(self):
        return self.infoHex    

    def setinfoHex(self, InfoFile):
        info = file(InfoFile,"rb")
        temp = info.readline().replace('\r\n', '\n').encode("hex")
        temp = temp + info.readline().replace('\r\n', '\n').encode("hex")
        temp = temp + info.readline().replace('\r\n', '\n').encode("hex")
        self.infoHex = temp
        del temp
        self.parse()
        
    def getdec(self, start, end, hexString=None):
        if (hexString == None):
            hexString = self.dataHexList[0]
        return int(hexString[(start*2):(2*end+2)],16)

    def parse(self):
        '''1. Searching for startcode = "e0c5ea" 
           2. parseDate, which follows allways direct behind the startcode
           3. A lot of DATA blocks until EOF or new startcode
           '''
        for DATA in self.dataHexList:
            tempdate = datetime((self.getdec(2,2,DATA)+2000), 
                                 self.getdec(0,0,DATA), 
                                 self.getdec(1,1,DATA),
                                 self.getdec(3,3,DATA),
                                 self.getdec(4,4,DATA))
            self.StartDateList.append(tempdate)
            self.DataDic = {}
            for i in range(5,(len(DATA[10:])/2)+5,5):
                print (tempdate + timedelta(0,minutes=((i-5)/5) ))                
                self.DataDic[(tempdate + timedelta(0,minutes=((i-5)/5) ))]=[self.getdec(i, i+1, DATA)/10.0,self.getdec(i, i+1, DATA)/1000.0,self.getdec(i, i, DATA)/100.0]
                # print "Min: %s min" % (i/5)
                # print "voltage: %s V" % (self.getdec(i, i+1, DATA)/10.0)
                # print "current: %s A" % (self.getdec(i, i+1, DATA)/1000.0)  
                # print "phase: %s %%" % (self.getdec(i, i, DATA)/100.0)
            
