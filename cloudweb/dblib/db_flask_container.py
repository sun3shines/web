# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import fullPath2id,id2treeAttrs,id2childAttrs

# cntList -> db_flask_container_list
 
def db_flask_container_list(db,atName,cntPath,tree):
    
    newPath = '/'.join([atName,cntPath])
    cid = fullPath2id(db, newPath)
    if 'true' == tree:
        return id2treeAttrs(db, cid)
    else:
        return id2childAttrs(db, cid)