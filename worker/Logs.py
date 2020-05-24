'''log the worker'''
import logging
import os


class WorkLog(object):
    __logger = logging.getLogger("WorkLog")
    __logger.setLevel(logging.WARNING)
    __fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    __sh = logging.StreamHandler()
    __fh = logging.FileHandler(filename=os.path.dirname(__file__),'worker.log'), encoding='utf-8')
    __sh.setFormatter(__fmt)
    __fh.setFormatter(__fmt)
    __logger.addHandler(__sh)
    __logger.addHandler(__fh)

    @classmethod
    def warn(cls,message):
        cls.__logger.warn(message)

    @classmethod
    def error(cls,message):
        cls.__logger.error(message)

    @classmethod
    def cri(cls,message):
        cls.__logger.cri(message)      
    
if __name__ == "__main__":
    config = LoadYaml.load(os.path.dirname(__file__),'worker.yaml')
    print(config)
    try:
        a = 1
        b = a + b
    except Exception as e:
        WorkLog.error(e)
