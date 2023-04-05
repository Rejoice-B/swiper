#原名 views.py
import traceback
from lib.http import render_json
from common import errors
from django.http import HttpRequest,HttpResponse

from lib.sms import send_verify_code
from lib.sms import check_vcode

from user.models import User,Profile
from user.forms import ProfileForm
def get_verify_code(request):
    '''手机注册'''

    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None)


def login(request):
    '''短信验证登录'''
    phonenum = request.GET.get('phonenum')
    vcode = request.GET.get('vcode')
    # print(phonenum,vcode)
    # return HttpResponse((phonenum, vcode))
    if not check_vcode(phonenum, vcode):#检查验证码
        user, created = User.objects.get_or_create(phonenum=phonenum)
        request.session['uid'] = user.id
        print(phonenum,vcode)

        return render_json(user.to_dict())
    else:
        return render_json(None, errors.VCODE_ERROR)

def loginText(request):
    '''取数据测试'''
    #
    # user, created= User.objects.get_or_create(phonenum="15034220710")
    # print(user.phonenum)
    # return render_json(user.to_dict())
    user = User.objects.all()
    data = []
    for item in user:
        data.append(item.to_dict())
    return render_json(data)

def delectUser(request):
    """删除某一条记录"""
    user = User.objects.filter(nickname="").delete()
    return HttpResponse(user.index())

def get_profile(request):
    '''获取个人资料'''
    pass

def show_profile(request):
    user = request.user
    return render_json(user.profile.to_dict())

def modify_profile(request):
    '''修改个人资料'''
    form = ProfileForm(request.POST)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.id = request.user.id
        profile.save()
        return render_json(profile.to_dict())
    else:
        return render_json(form.errors,errors.PROFILE_ERROR)

def upload_avatar(request):
    '''头像上传'''
    pass
