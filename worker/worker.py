'''
used update acess_toekn
'''
import requests,json
from  modles.acess_token import AcessToken
from Logs import WorkLog


class GetAcessToken(object):
    def __init__(self,appid,secret,*args,**kwargs):
        pass

    def __gettoken(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            'grant_type'：'client_credential',
            'appid': None,
            'secret': None
        }
        try:
            res = requests.get(url=url,params=data).json
            self.__storetoken(json.loads(res).get('access_token',''))
        except Exception as e:
            WorkLog.error(e)
    
    def __storetoken(self,token):
        if token:
            pass
        else:
            message = 'can not find acess token'
            WorkLog.error(message)        
    def updatetoken(self):
        self.__gettoken()

if __name__ == "__main__":
    pass