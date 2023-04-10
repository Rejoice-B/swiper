from django.db import models
from lib.orm import ModelMixin
# Create your models here.
class Vip(models.Model,ModelMixin):
    name = models.CharField(max_length=16,unique=True)
    level = models.IntegerField(unique=True)
    price = models.FloatField()

    class Meta:
        ordering = ['level'] # 以level做排序

    def permissions(self):
        '''当前 VIP 具有的所有权限'''
        relation = VipPermRelation.objects.filter(vip_id=self.id)
        perm_id_list = [r.perm_id for r in relation]
        return Permission.objects.filter(id__in=perm_id_list)

    def has_perm(self,perm_name):
        '''检查该等级 VIP 是否具有某权限'''
        try:
            perm = Permission.objects.get(name=perm_name)
        except Permission.DoesNotExist: # 如果权限名称不对，返回False
            return False
        else: # 如果有这样一个权限就搜索这样一个关系
            return VipPermRelation.objects.filter(vip_id=self.id,perm_id=perm.id).exists()

class Permission(models.Model,ModelMixin):
    name = models.CharField(max_length=32)
    desc = models.TextField()

class VipPermRelation(models.Model):
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()