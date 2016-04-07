# -*- coding: utf-8 -*-

import hashlib

def str2uuid(str):
    
    m = hashlib.md5()  
    m.update(str)
    return m.hexdigest()