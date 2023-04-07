#!C:\Program Files\Python310\python
import sys

import django
import os
import random
from pathlib import Path

#设置环境
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")
django.setup()

from user.models import User
#from vip.models import Vip,Permission,VippermRelation

last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)
first_names = {
    '男': [
        '高运','翰彦','辰野','道梓','昌睿',
        '俊元','宇尉','霖良','灿景','鸿博',
        '晓文','惟光','冠翰','崇景','文瑾',
        '清颜','学裕','锐右','明博','恺南',
        '立旭','柯玮','颜皓','杰宁','毅乐'
    ],
    '女': [
        '霏怡','雅诗','凝如','筠枫','蕴齐',
        '媛楚','小妙','芯融','萱春','阳雪',
        '馨静','凝湘','凝云','香怡','宜涵',
        '雅奇','柔婉','梦媛','夏雅','菡芝',
        '流蕾','仪梦','丽愫','韶丹','映婕'
    ]
}

def random_name():
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    return ''.join([last_name,first_name]), sex

def create_robots(n):
    # 创建初始用户
    for i in range(n):
        name, sex = random_name()
        try:
            User.objects.create(
                phonenum='%s'% random.randrange(21000000000,21900000000),
                nickname=name,
                sex=sex,
                birth_year=random.randint(1980,2000),
                birth_month=random.randint(1,12),
                birth_day=random.randint(1,28),
                location=random.choice(['北京','上海','深圳','成都','西安','沈阳','武汉']),
            )
            print('created: %s %s' % (name,sex))
        except django.db.utils.IntegrityError:
            pass

if __name__ == '__main__':
    create_robots(400)