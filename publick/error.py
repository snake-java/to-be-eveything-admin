'''define error'''

class ConfigError(Exception):
    def __init__(self,err_message):
        self.err_message = err_message

class NetworkError(RuntimeError):
    def __init__(self,err_message):
        self.err_message = err_message
    