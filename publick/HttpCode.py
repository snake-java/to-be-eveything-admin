'''
define the httpcode
'''

class Code:
    OK = '4000'
    DATAERR = '4001'
    PARAERR = '4002'
    
ERR_MAP = {
    Code.OK: '成功',
    Code.DATAERR: "数据库错误"，
    Code.PARAERR："参数错误"
}

    