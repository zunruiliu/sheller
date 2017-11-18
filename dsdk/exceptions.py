# -*- coding:utf-8 -*-

from libs.errorcode import CommonError

'''只定义最基础的exception，业务级exception直接初始化APIError，*不要*再定义新业务级exception'''


class ImproperlyConfigured(Exception):
    """Django is somehow improperly configured"""
    pass


class APIError(Exception):
    '''业务级exception直接初始化此类，*不要*再定义新业务级exception类'''
    statuscode = CommonError.UNKNOWN

    def __init__(self, statuscode=None, msg=None):
        if statuscode is not None:
            self.statuscode = statuscode
        if msg is not None:
            self.statuscode.msg = msg

    def __repr__(self):
        return '%s(code=%r, message=%r)' % (self.__class__,
                                            self.statuscode.code,
                                            self.statuscode.msg)

    def as_dict(self):
        return {'code': self.statuscode.code, 'msg': self.statuscode.msg}


class RequestMethodError(Exception):
    def __repr__(self):
        return "request method not allowed."