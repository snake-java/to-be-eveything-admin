import requests

class GetAcessToken(object):
    def __init__(self,*args,**kwargs):
        pass

    def __gettoken(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            
        }
        res = requests.get(url=url,params=data)