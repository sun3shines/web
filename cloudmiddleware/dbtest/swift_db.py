
from cloudweb.db.table.mysql import getDb
from cloudweb.db.container import cntdelete,cntput

def container_put_test(path):
    conn = getDb()
    cntput(path,conn)
    