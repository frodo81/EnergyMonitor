def getdec(hexString, start, end):
    return int(s[(start*2):(2*end+2)],16)

info = file('TestFiles/a01307fe.bin',"rb")

firstline = info.readline().replace('\r\n', '\n').encode("hex")
secondline = info.readline().replace('\r\n', '\n').encode("hex")
thirdline = info.readline().replace('\r\n', '\n').encode("hex")
s = firstline + secondline + thirdline
# Total power and times
print "Total power consumption: %s kWh" % (getdec(s, 5, 7)/1000.0)
print "Total recorded time: %s h" % (getdec(s, 8, 10)/100.0)
print "Total ON time: %s h" % (getdec(s, 11, 13)/100.0)
# Total power values
print "Total kwh (today): %s kwh" % (getdec(s, 14, 16)/1000.0)
print "Total kwh (yesterday): %s kwh" % (getdec(s, 17, 19)/1000.0)
print "Total kwh (2 days ago): %s kwh" % (getdec(s, 20, 22)/1000.0)
print "Total kwh (3 days ago): %s kwh" % (getdec(s, 23, 25)/1000.0)
print "Total kwh (4 days ago): %s kwh" % (getdec(s, 26, 28)/1000.0)
print "Total kwh (5 days ago): %s kwh" % (getdec(s, 29, 31)/1000.0)
print "Total kwh (6 days ago): %s kwh" % (getdec(s, 32, 34)/1000.0)
print "Total kwh (7 days ago): %s kwh" % (getdec(s, 35, 37)/1000.0)
print "Total kwh (8 days ago): %s kwh" % (getdec(s, 38, 40)/1000.0)
print "Total kwh (9 days ago): %s kwh" % (getdec(s, 41, 43)/1000.0)
# Total recorded times
print "Total recorded time (today): %s h" % (getdec(s,44,45)/100.0)
print "Total recorded time (yesterday): %s h" % (getdec(s,46,47)/100.0)
print "Total recorded time (2 days ago): %s h" % (getdec(s,48,49)/100.0)
print "Total recorded time (3 days ago): %s h" % (getdec(s,50,51)/100.0)
print "Total recorded time (4 days ago): %s h" % (getdec(s,52,53)/100.0)
print "Total recorded time (5 days ago): %s h" % (getdec(s,54,55)/100.0)
print "Total recorded time (6 days ago): %s h" % (getdec(s,56,57)/100.0)
print "Total recorded time (7 days ago): %s h" % (getdec(s,58,59)/100.0)
print "Total recorded time (8 days ago): %s h" % (getdec(s,60,61)/100.0)
print "Total recorded time (9 days ago): %s h" % (getdec(s,62,63)/100.0)
# Total ON times
print "Total ON time (today): %s h" % (getdec(s,64,65)/100.0)
print "Total ON time (yesterday): %s h" % (getdec(s,66,67)/100.0)
print "Total ON time (2 days ago): %s h" % (getdec(s,68,69)/100.0)
print "Total ON time (3 days ago): %s h" % (getdec(s,70,71)/100.0)
print "Total ON time (4 days ago): %s h" % (getdec(s,72,73)/100.0)
print "Total ON time (5 days ago): %s h" % (getdec(s,74,75)/100.0)
print "Total ON time (6 days ago): %s h" % (getdec(s,76,77)/100.0)
print "Total ON time (7 days ago): %s h" % (getdec(s,78,79)/100.0)
print "Total ON time (8 days ago): %s h" % (getdec(s,80,81)/100.0)
print "Total ON time (9 days ago): %s h" % (getdec(s,82,83)/100.0)
# ID Number
print "ID number: %s" % getdec(s,84,84)
# Tarif information
print "Tarif 1: %s Euro" % (getdec(s,85,88)/1000.0)
print "Tarif 2: %s Euro" % (getdec(s,89,92)/1000.0)
# Clock information
print "Hour (initial setting): %s h" % getdec(s,93,93)
print "Minute (initial setting): %s min" % getdec(s,94,94)

print "Month (initial setting): %s" % getdec(s,95,95)
print "Day (initial setting): %s" % getdec(s,96,96)
print "Year (initial setting): %s" % (2000 + getdec(s,97,97))



