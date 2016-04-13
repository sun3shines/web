# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import fullPath2id,update_stobj

# disableOt -> db_flask_object_disable 
# enableOt -> db_flask_object_enable

def db_flask_object_disable(db,newPath):

    # objPath 为restful时，则为/normal/test.txt
    # objPath 为db时，则为 account/normal/test.txt ?? search 时有db操作。但是不是路径。
    
    oid = fullPath2id(db,newPath)
    return update_stobj(db,oid,state='disable')

def db_flask_object_enable(db,newPath):
    
    oid = fullPath2id(db,newPath)
    return update_stobj(db,oid,state='enable')
