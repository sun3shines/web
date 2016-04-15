
import os
from cloudweb.db.table.mysql import getDb

if __name__ == '__main__':
    cmd = 'rm -rf /mnt/cloudfs-object/testadministrator163com/;rm -rf /mnt/cloudfs-object/AUTH_testadministrator163com.db'
    os.system(cmd)
    sql = " delete from user where name='AUTH_testadministrator163com'"
    db = getDb()
    db.execute_sql(sql)
    sql2 = "delete from stobj where path = 'AUTH_testadministrator163com'"
    db.execute_sql(sql2)
