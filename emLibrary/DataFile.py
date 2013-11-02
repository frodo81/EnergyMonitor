'''
Created on 01.11.2013

@author: bernd
'''

from datetime import datetime, timedelta

class DataFile(object):
    '''
    classdocs
    '''
    def __init__(self,DataFile):
        '''
        Constructor
        '''        
        with open(DataFile, 'rb') as content_file:
            content = content_file.read()
        temp = content.replace('\r\n', '\n').encode("hex")
        self.dataHexList = temp[:temp.find('ffffffff')].split("e0c5ea")[1:]
        self.StartDateList = []
        self.parse()

    def getdataHexList(self):
        return self.dataHexList    

    def getStartDateList(self):
        return self.StartDateList    

    def setinfoHex(self, InfoFile):
        '''Do not use at the moment, is only a copy form InfoFile class!'''
        info = file(InfoFile,"rb")
        temp = info.readline().replace('\r\n', '\n').encode("hex")
        temp = temp + info.readline().replace('\r\n', '\n').encode("hex")
        temp = temp + info.readline().replace('\r\n', '\n').encode("hex")
        self.infoHex = temp
        del temp
        self.parse()
        
    def getdec(self, start, end, hexString=None):
        '''Decode the byte parameter(s) of hexString to an Integer. 
           This function calls the global object datahexList[0] string for default.
           Only need The 2 Bytes like in the protocol paper from voltcraft.  
        '''        
        if (hexString == None):
            hexString = self.dataHexList[0]
        return int(hexString[(start*2):(2*end+2)],16)

    def parse(self):
        '''This function parses date, time and data out of a the DATA blob. 
           Save initial date and time in a python datetime object and the voltage, 
           current and phase information in a dictionary with the correct
           datetime information as key 
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
                self.DataDic[(tempdate + timedelta(0,minutes=((i-5)/5) ))]=[self.getdec(i, i+1, DATA)/10.0,self.getdec(i+2, i+3, DATA)/1000.0,self.getdec(i+4, i+4, DATA)/100.0]     
