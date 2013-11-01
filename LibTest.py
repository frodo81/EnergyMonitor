'''
Created on 01.11.2013

@author: bernd
'''
import unittest
from emLibrary.InfoFile import InfoFile


class Test(unittest.TestCase):


    def testConstructor(self):
        print "Starting testConstructor ..."
        testobject = InfoFile("TestFiles/a01307fe.bin")
        print "    " + testobject.infoHex
        print "Finished testConstructor sucessfully!\n"
        
    def testValue(self):        
        print "Starting testValue ..."
        print "  Test with 2 params"
        testobject = InfoFile("TestFiles/a01307fe.bin")
        print "    %s" % (testobject.getdec(5, 7)/1000.0)
        print "    %s" % (testobject.getdec(8, 10)/100.0)
        print "  Test with 3 params"
        print "    %s" % (testobject.getdec(5,7,"494e464f3a000a4d00d4420065280001530000a60001020000b200000b00000a00008f0000b70000d20000c70415071c0960096009600960096009600960096004130654044504a90729067307a706b503f60420000002000000020000133305100dffffffff")/1000.0)
        print "Finished testValue sucessfully!\n"

    def testAttributes(self):
        print "Starting testAttributes ..."
        testobject = InfoFile("TestFiles/a01307fe.bin")
        print "  Total power and times"
        print "    Total power: %s kWh" % testobject.TotalPower
        print "    Total recorded time: %s h" % testobject.TotalRecTime
        print "    Total ON time: %s h" % testobject.TotalONTime
        print "  Total power values"
        print "    as List: "
        print "      " + str(testobject.Totalkwh)
        print "    as value: "
        print "      Total kwh (today): %s kwh" % testobject.Totalkwh[0]
        print "      Total kwh (yesterday): %s kwh" % testobject.Totalkwh[1]
        print "      Total kwh (2 days ago): %s kwh" % testobject.Totalkwh[2]
        print "      Total kwh (3 days ago): %s kwh" % testobject.Totalkwh[3]
        print "      Total kwh (4 days ago): %s kwh" % testobject.Totalkwh[4]
        print "      Total kwh (5 days ago): %s kwh" % testobject.Totalkwh[5]
        print "      Total kwh (6 days ago): %s kwh" % testobject.Totalkwh[6]
        print "      Total kwh (7 days ago): %s kwh" % testobject.Totalkwh[7]
        print "      Total kwh (8 days ago): %s kwh" % testobject.Totalkwh[8]
        print "      Total kwh (9 days ago): %s kwh" % testobject.Totalkwh[9]
        print "  Total recorded times values"
        print "    as List: "
        print "      " + str(testobject.TotalRecTimeList)
        print "    as value: "
        print "      Total recorded time (today): %s h" % testobject.TotalRecTimeList[0]
        print "      Total recorded time (yesterday): %s h" % testobject.TotalRecTimeList[1]
        print "      Total recorded time (2 days ago): %s h" % testobject.TotalRecTimeList[2]
        print "      Total recorded time (3 days ago): %s h" % testobject.TotalRecTimeList[3]
        print "      Total recorded time (4 days ago): %s h" % testobject.TotalRecTimeList[4]
        print "      Total recorded time (5 days ago): %s h" % testobject.TotalRecTimeList[5]
        print "      Total recorded time (6 days ago): %s h" % testobject.TotalRecTimeList[6]
        print "      Total recorded time (7 days ago): %s h" % testobject.TotalRecTimeList[7]
        print "      Total recorded time (8 days ago): %s h" % testobject.TotalRecTimeList[8]
        print "      Total recorded time (9 days ago): %s h" % testobject.TotalRecTimeList[9]      
        
        print "  Total ON times values"
        print "    as List: "
        print "      " + str(testobject.TotalONTimeList)
        print "    as value: "        
        print "      Total ON time (today): %s h" % testobject.TotalONTimeList[0]
        print "      Total ON time (yesterday): %s h" % testobject.TotalONTimeList[1]
        print "      Total ON time (2 days ago): %s h" % testobject.TotalONTimeList[2]
        print "      Total ON time (3 days ago): %s h" % testobject.TotalONTimeList[3]
        print "      Total ON time (4 days ago): %s h" % testobject.TotalONTimeList[4]
        print "      Total ON time (5 days ago): %s h" % testobject.TotalONTimeList[5]
        print "      Total ON time (6 days ago): %s h" % testobject.TotalONTimeList[6]
        print "      Total ON time (7 days ago): %s h" % testobject.TotalONTimeList[7]
        print "      Total ON time (8 days ago): %s h" % testobject.TotalONTimeList[8]
        print "      Total ON time (9 days ago): %s h" % testobject.TotalONTimeList[9]
        print "  ID Number"
        print "    ID number: %s" % testobject.ID
        print "  Tarif information"
        print "    Tarif 1: %s Euro" % testobject.Tarif1
        print "    Tarif 2: %s Euro" % testobject.Tarif2
        print "  Date and time information"
        print "    Initial Date and time: %s " % testobject.InitialDate               
        print "Finished testAttributes sucessfully!\n"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConstructor']
    unittest.main()