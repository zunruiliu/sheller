# -*- coding:utf-8 -*-

'''
工具
'''


def valid_ip(ip):
    '''
    校验ip格式
    :return --格式正确返回true，错误返回false
    校验规则：
    ip地址第四位是'.'
    '''
    if ip[3] != '.':
        return False
    return True
