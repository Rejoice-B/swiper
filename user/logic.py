import random

import requests
from django.core.cache import cache

from swiper import config
from worker import call_by_worker
from worker import celery_app

def gen_verify_code(length=6):
    '''产生一个验证码'''
    return random.randrange(10 ** (length-1),10 ** length)

@call_by_worker
def send_verify_code(phonenum):
    '''发送一个验证码'''
    vcode=gen_verify_code()
    # key='VerifyCode-%s' % phonenum
    # cache.set(key,vcode,120)#缓存，验证码时效120
    sms_cfg=config.HY_SMS_PARAMS.copy()
    sms_cfg['content']=sms_cfg['content'] % vcode
    sms_cfg['mobile'] = phonenum
    response=requests.post(config.HY_SMS_URL,data=sms_cfg)
    return response

def check_vode(phonenum, vcode):
    '''检查验证码'''
    cached_vode =  cache.get('VCode-%s' % phonenum)
    return cached_vode == vcode
