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
    mypath = 'TestFiles'
    files = [ mypath + "/" + f for f in listdir(mypath) if (isfile(join(mypath,f)) and f.endswith('.bin')) ]
    for i in files:
        try:
            emDF.DataFile(i).toSqlDB(mysqldb.load_DB_params(configFile))
            print "Finished with tile: %s. " % i
        except:
            print "Fault with %s, maybe a Info File!" % i
        
        
    