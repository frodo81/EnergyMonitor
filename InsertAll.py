'''
Created on 03.11.2013

@author: bernd
'''

if __name__ == '__main__':
    import emLibrary.DataFile as emDF
    from os import listdir
    from os.path import isfile, join
    import mysqldb.mysqldb as mysqldb
    configFile = 'em.config'    
    mypath = '/home/bernd/git/EnergyMonitor/Messfiles/2013-11-26 ID 0'
    files = [ mypath + "/" + f for f in listdir(mypath) if (isfile(join(mypath,f)) and (f.endswith('.bin') or f.endswith('.BIN'))) ]
    print files
    for i in files:
        try:
            db, user, passwd, host = mysqldb.load_DB_params(configFile) 
            print db, user, passwd, host  
            con = mysqldb.con_init(host, user, passwd, db)
            emDF.DataFile(i).toSqlDB(con)
            #print "Now do con.query"
            # con.execute("SET AUTOCOMMIT=0")
            #v = con.execute("""INSERT INTO `test`.`PandasTest` 
            #         (`DateTime`, `Voltage`, `Current`, `Phase`) 
            #     VALUES ('2013-11-13 19:05:00', 236.0, 0.0, 0.0);""")
            #print "con.query done"
            #print "Now do con.commit"
            # con.execute("COMMIT")        
            #print "con.commit done"
            print "Finished with tile: %s. " % i
            mysqldb.con_close(con)
        except:
            print "Fault with %s, maybe a Info File!" % i

        
        
    
