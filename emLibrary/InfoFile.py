'''
Created on 01.11.2013

@author: bernd
'''

from datetime import datetime

class InfoFile(object):
    '''
    classdocs
    '''
    def __init__(self,InfoFile):
        '''
        Constructor
        '''
        info = file(InfoFile,"rb")
        temp = info.readline().replace('\r\n', '\n').encode("hex")
        temp = temp + info.readline().replace('\r\n', '\n').encode("hex")
        temp = temp + info.readline().replace('\r\n', '\n').encode("hex")
        self.infoHex = temp
        del temp
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
            hexString = self.infoHex
        return int(hexString[(start*2):(2*end+2)],16)

    def parse(self):
        self.TotalPower = self.getdec(5, 7)/1000.0
        self.TotalRecTime = self.getdec(8, 10)/100.0
        self.TotalONTime = self.getdec(11, 13)/100.0
        self.Totalkwh = []
        for i in range(14,42,3):
            self.Totalkwh.append(self.getdec(i, i+2)/1000.0)
        self.TotalRecTimeList = []
        for i in range(44,63,2):
            self.TotalRecTimeList.append(self.getdec(i, i+1)/100.0)
        self.TotalONTimeList = []
        for i in range(64,83,2):
            self.TotalONTimeList.append(self.getdec(i, i+1)/100.0)
        self.InitialDate = datetime((2000 + self.getdec(97,97)),
                                    self.getdec(95,95),
                                    self.getdec(96,96),
                                    self.getdec(93,93),
                                    self.getdec(94,94)
                                    )
        self.ID = self.getdec(84,84)
        self.Tarif1 = self.getdec(85,88)/1000.0
        self.Tarif2 = self.getdec(89,92)/1000.0
