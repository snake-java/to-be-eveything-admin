'''
load the config
'''
import yaml
import os


class LoadYaml(object):
    def __init__(self):
        pass

    @classmethod
    def load(self,path=None,file='config/config.yaml'):
        '''
        load the yaml
        '''
        file =os.path.join(os.path.dirname(__file__),file) if not path else os.path.join(path,file)
        
        with open(file,'r',encoding='utf-8') as f:
            stream = f.read()
        try:
            return yaml.load(stream)
        except Exception as e:
            return dict() 



