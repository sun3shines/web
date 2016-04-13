# -*- coding: utf-8 -*-

from cloudweb.db.table.stobj import fullPath2id,id2treeAttrs,id2childAttrs

# drList -> db_flask_container_list

def db_flask_container_list(db,atName,drPath,tree):
    
    newPath = '/'.join([atName,drPath])
    did = fullPath2id(db,newPath)
    if 'true' == tree:
        return id2treeAttrs(db, did)
    else:
        return id2childAttrs(db, did)
