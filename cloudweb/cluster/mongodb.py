
from pymongo import MongoClient
from clusterConfig import mongoHost,mongoPort,mongoDb,memCache
from pyLock import getLock

# object 
def getDB(host,port,dbName):
    client = MongoClient(host,port)
    dbObj = client[dbName]
    return dbObj

def getCollection(dbObj,tableName):
    return dbObj[tableName]

def getSeqFromTable(dbObj,tableName,seqName):
    print '111'
    seqList = [elmDict[seqName] for elmDict in dbObj[tableName].find({},{seqName:1,'_id':0})]
    seqList.sort()
    return seqList[-1]

def getDocFromTable(dbObj,tableName,seqName,blockName,filter={}):
    print '222' 
    seqList = [(elmDict[seqName],elmDict[blockName],elmDict['_id']) for elmDict in dbObj[tableName].find(filter)]
    seqList.sort(key=lambda elm :elm[0])
    if len(seqList)>0:
        return seqList[0]
    return None

def getSeq(seqDict):

    dbObj = seqDict.get('dbObj')
    tableName = seqDict.get('tableName')
    seqName = seqDict.get('seqName')

    seqInt = memCache.get('%s%s'%(tableName,seqName))
    if not seqInt:
        seqInt = getSeqFromTable(dbObj,tableName,seqName)
    if not seqInt:
        seqInt = 0
    return seqInt

def getAccessSeq(seqDict):
   
    seqDict['Desc'] = 'Access'

    print seqDict['Desc'],seqDict['dbObj'],seqDict['tableName'],seqDict['seqName'],seqDict['blockName']

    seqInt = memCache.get('%s%s%s'%(seqDict['Desc'],seqDict['tableName'],seqDict['seqName']))
    if not seqInt:
        elmTuple = getDocFromTable(seqDict['dbObj'],seqDict['tableName'],seqDict['seqName'],seqDict['blockName'],filter={'accessed':False})
        if not elmTuple:
            return
        seqInt = elmTuple[0]
        setDescSeq(seqDict,seqInt)

    return seqInt

def setDescSeq(seqDict,seqInt):
   
    lock = getLock(seqDict['tableName'])
    if lock.acquire():
        memCache['%s%s%s'%(seqDict['Desc'],seqDict['tableName'],seqDict['seqName'])] = seqInt
        lock.release()

def getDoc(dbObj,tableName,filter={}):
    elmList = [elmDict for elmDict in dbObj[tableName].find(filter)]
    return elmList

def updateDoc(dbObj,tableName,filter,updateDict):
    dbObj[tableName].update(filter,{'$set':updateDict})

if __name__ == '__main__':

    dbObj = getDB(mongoHost,mongoPort,mongoDb)
#    tableObj = getCollection(dbObj,'messages')
#    postDict = {'block':'xxx','seq':2,'accessed':False}
#    post_id = tableObj.insert(postDict)
#    print post_id
#    print getSeqFromTable(dbObj,'messages','seq')

#    seqDict = {'dbObj':dbObj,'tableName':'messages','seqName':'seq'}
#    seqInt = getSeq(seqDict)
#    print seqInt
#    seqInt = seqInt + 1 
#    setDescSeq(seqDict.update({'Desc':'Insert'}),seqInt)
#    print getSeq(seqDict)

    seqDict = {}
    seqDict['dbObj'] = dbObj
    seqDict['tableName'] = 'messages'
    seqDict['seqName'] = 'seq'
    seqDict['blockName'] = 'block'
    seqInt = getAccessSeq(seqDict)
    print seqInt
    seqInt = getAccessSeq(seqDict)
    print seqInt
    
    elmList = getDoc(dbObj,'messages',filter={'seq':seqInt})
    if elmList:
        print elmList[0]

    updateDoc(dbObj,'messages',{'seq':seqInt},{'accessed':True})
    seqDict = {'tableName':'messages','seqName':'seq','Desc':'Access'}
    seqInt = seqInt + 1
    setDescSeq(seqDict,seqInt)

