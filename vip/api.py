from lib.http import render_json
from vip.models import Vip
# Create your views here.
def show_vip_permissions(request):
    vip_permissions = []
    for vip in Vip.objects.filter(level__gte=1): # level__gte=1是level大于等于1的意思
        vip_info = vip.to_dict()
        perm_info = [] # 权限的信息封装到这个列表中
        for perm in vip.permissions():
            perm_info.append(perm.to_dict())
        vip_info['perm_info'] = perm_info
        vip_permissions.append(vip_info)
    return render_json(vip_permissions)