# -*- coding: utf-8 -*-

import subprocess
import json
from StringIO import StringIO

def filter_hw(hw, cl):
    res = []
    if "children" in hw:
        for child in hw["children"]:
            if child["class"] == cl:
                res.append(child)
                continue
            else:
                res.extend(filter_hw(child, cl))
    return res


def get_hw():  
    output = subprocess.Popen(['lshw', '-json'], stdout=subprocess.PIPE).communicate()[0]
    hw_io = StringIO(output)
    hw = json.load(hw_io)    
    return hw


