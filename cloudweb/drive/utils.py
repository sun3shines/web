
import json
from cloudweb.globalx.variable import GLOBAL_USER_TOKEN
from cloudlib.common.bufferedhttp import jresponse
from cloudlib.restful.cloudfs.lib_token import libGetToken

def getAtName(request):
    param = json.loads(request.body)
    atName = ''
    if param.has_key('objPath'):
        atName = param.get('objPath').split('/')[0]
    elif param.has_key('srcNewPath'):
        atName = param.get('srcNewPath').split('/')[0]
    elif param.has_key('newPath'):
        atName = param.get('newPath').split('/')[0]
    else:
        return False,'param error,no account name found'
    return True,atName

def getUserToken(atName,request):
    
    token = GLOBAL_USER_TOKEN.get_user_token(atName)
    if not token:
        user_info = GLOBAL_USER_TOKEN.get_user_info(atName)
        if not user_info:
            return False,jresponse('-1', 'user does not login,please login', request, 400)
        token = libGetToken(user_info.get(GLOBAL_USER_TOKEN.email),user_info.get(GLOBAL_USER_TOKEN.passwd))
        if not token:
            GLOBAL_USER_TOKEN.eliminate(atName)
            return False,jresponse('-1', 'get user token failed,check password or token server', request, 400)
        GLOBAL_USER_TOKEN.put(atName, user_info.get(GLOBAL_USER_TOKEN.email), user_info.get(GLOBAL_USER_TOKEN.passwd), token)
    return True,token


def getAtNameByEmail(email):

        return 'AUTH_' + email.replace('@','').replace('.','')
     