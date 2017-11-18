# -*- coding:utf-8 -*-


from libs.errorcode import CommonError, StatusCode


class ERRORCODE(CommonError):
    '''错误码
    业务级别的错误码
    '''

    IP_BASE = 10000
    INVALID_IP_ADDRESS = StatusCode(IP_BASE + 1, 'INVALID_IP_ADDRESS', u'非法IP地址')