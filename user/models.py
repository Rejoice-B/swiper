from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    '''用户数据模型'''
    SEX = (('男','男'),('女','女'))
    nickname = models.CharField(max_length=32,unique=True)
    phonenum = models.CharField(max_length=16,unique=True)
    sex = models.CharField(default='女',max_length=8,choices=SEX)
    birth_year = models.IntegerField(default=2000, verbose_name='出生年')
    birth_month = models.IntegerField(default=1, verbose_name='出生月')
    birth_day = models.IntegerField(default=1, verbose_name='出生日')
    avatar=models.CharField(max_length=256, verbose_name='个人形象')
    location=models.CharField(max_length=32, verbose_name='常居地')

    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        # return (today-birth_date).days // 365
        times = today - birth_date
        return times.days // 365

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'phonenum': self.phonenum,
            'age': self.age,
            'sex': self.sex,
            'avatar':self.avatar,
            'location': self.location,

        }

    @property
    def profile(self):#构建对Profile表的关联
        '''用户的配置项'''
        if not hasattr(self,'_profile'):#'_profile'是否在self的属性中
            self._profile,_ = Profile.objects.get_or_create(id=self.id)#直接把结果放到对象
            #self._profile=_profile#把_profile变成一个属性
        return self._profile
'''from user.models import User,Profile'''
'''ll=User.objects.create(nickname='LLHH',phonenum='199990000000')'''

class Profile(models.Model):
    '''用户配置项'''

    SEX = (('男', '男'), ('女', '女'))
    dating_sex = models.CharField(default='男',max_length=8, choices=SEX, verbose_name='匹配的性别')

    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小查找范围')
    max_distance = models.IntegerField(default=10, verbose_name='最大查找范围')


    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')#调试失败
    max_dating_age = models.IntegerField(default=45, verbose_name='最大交友年龄')#调试失败

    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True, verbose_name='不让匹配的人看我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放视频')

    def to_dict(self):
        return {
        'id': self.id,
        'dating_sex': self.dating_sex,
        'location': self.location,
        'min_distance': self.min_distance,
        'max_distance': self.max_distance,
        'min_dating_age': self.min_dating_age,
        'max_dating_age': self.max_dating_age,
    }
