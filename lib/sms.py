import random

import requests
from django.core.cache import cache

from swiper import config
from worker import call_by_worker
#from worker import celery_app

from common.errors import VcodeExist
def gen_verify_code(length=6):
    '''产生一个验证码'''
    return random.randrange(10 ** (length-1),10 ** length)

import time

@call_by_worker
def send_sms(phonenum, msg):
    '''发送短信'''
    params = config.HY_SMS_PARAMS.copy()
    params['content'] = params['content'] % msg
    params['mobile'] = phonenum
    response=requests.post(config.HY_SMS_URL,data=params)
    return response


def send_verify_code(phonenum):
    '''发送一个验证码'''
    key='VerifyCode-%s' % phonenum
    if not cache.has_key(key):
        vcode = gen_verify_code()
        send_sms(phonenum, vcode)
        #response=requests.post(config.HY_SMS_URL,data=params)
        cache.set(key, vcode, 300)#缓存，验证码时效300
    else:
        raise VcodeExist

def check_vcode(phonenum, vcode):
    '''检查验证码'''
    # cached_vcode =  cache.get('VCode-%s' % phonenum)
    cached_vcode = 452802
    return cached_vcode == vcode
