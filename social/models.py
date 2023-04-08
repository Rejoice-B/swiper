from django.db import models
from django.db.models import Q
# Create your models here.

class Swiped(models.Model):
    '''滑动记录'''
    FLAGS = (
        ('superlike','上海'),
        ('like','右滑'),
        ('dislike','左滑')
    )
    uid = models.IntegerField(verbose_name='滑动者的UID')
    sid = models.IntegerField(verbose_name='被滑动者的UID')
    flag = models.CharField(max_length=10, choices=FLAGS)
    dtime = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'dtime'

    @classmethod
    def like(cls,uid,sid):
        obj = cls.objects.create(uid=uid,sid=sid,flag='like')
        return obj

    @classmethod
    def superlike(cls,uid,sid):
        obj = cls.objects.create(uid=uid,sid=sid,flag='superlike')
        return obj

    @classmethod
    def dislike(cls,uid,sid):
        obj = cls.objects.create(uid=uid,sid=sid,flag='dislike')
        return obj

    # @classmethod
    # def rewind(cls,uid):
    #     '''撤销'''
    #     cls.objects.filter(uid=uid).latest().delete()# 找到上一次操作的，最新添加的一个,然后删除

    @classmethod
    def is_liked(cls,uid,sid):
        '''判断喜欢是否存在 '''
        return cls.objects.filter(uid=uid,sid=sid,flag__in=['superlike','like']).exists()# 判断喜欢是否存在

    @classmethod
    def liked_me(cls,uid):
        '''找到喜欢我得人'''
        return cls.objects.filter(sid=uid,flag__in=['superlike','like'])

class Friend(models.Model):
    '''好友关系'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def make_friends(cls,uid1,uid2):
        ''' 建立好友关系'''
        uid1, uid2 = sorted([uid1,uid2]) # 排序为了防止重复的喜欢数据
        cls.objects.get_or_create(uid1=uid1,uid2=uid2)

    @classmethod
    def is_friends(cls,uid1,uid2):
        '''是否存在好友关系'''
        uid1, uid2 = sorted([uid1, uid2])  # 排序为了防止重复的喜欢数据
        return cls.objects.filter(uid1=uid1, uid2=uid2).exists() # 两人是否存在好友关系

    @classmethod
    def friend_id_list(cls,uid):
        '''获取用户所有的好友的uid列表'''
        #查询用户的好友关系
        condition = Q(uid1=uid) | Q(uid2=uid)
        relations = cls.objects.filter(condition)
        #筛选好友的uid
        id_list = []
        for relation in relations:
            friend_id = relation.uid2 if relation.uid1 == uid else relation.uid1
            id_list.append(friend_id)
        return id_list

    @classmethod
    def break_off(cls,uid1,uid2):
        '''删除好友关系 '''
        uid1, uid2 = sorted([uid1, uid2])  # 排序为了防止重复的喜欢数据
        cls.objects.filter(uid1=uid1, uid2=uid2).delete()  # 删除好友关系