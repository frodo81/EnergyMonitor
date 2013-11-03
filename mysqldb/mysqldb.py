'''
Created on 27.12.2011

@author: bernd
'''
import MySQLdb as mysql

def con_init(host,user,passwd,db):
    con = mysql.connect(host,user,passwd,db)
    cur = con.cursor()
    return cur

def load_DB_params(configFile):
    f = open(configFile, 'r')
    db, dbuser, passwd, host = "", "", "", ""
    for line in f:
        line = line.replace("\n","").split("=",1)             
        if line[0]=="db":   
            del line[0]
            db = line[0]                                 
        if line[0]=="dbuser":
            del line[0]
            dbuser = line[0]
        if line[0]=="passwd":
            del line[0]
            passwd = line[0]                                
        if line[0]=="host":
            del line[0]
            host = line[0]
    return db, dbuser, passwd, host

def con_close(con):
    con.close()
    print "MYSQL Verbindung closed"
