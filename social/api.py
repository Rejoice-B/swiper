from lib.http import render_json

from social.logic import rcmd_users
from user.models import User

# Create your views here.
def get_rcmd_users(request):
    '''获取推荐列表'''
    user = request.user
    page = int(request.GET.get('page', 1)) # 页码
    per_page = 10 # 每页显示的数量
    start = (page - 1) * per_page # 每页显示的数量的开头一个
    end = start + per_page # 每页显示的数量的最后一个
    users = rcmd_users(user)[start:end] # 匹配的所有用户
    result = [u.to_dict() for u in users]
    #result.insert(0,user)
    return render_json(result)
def like(request):
    '''喜欢'''
    return render_json(None)
def superlike(request):
    '''超级喜欢'''
    return render_json(None)
def dislike(request):
    '''不喜欢'''
    return render_json(None)
def rewind(request):
    '''反悔'''
    return render_json(None)
def show_liked_me(request):
    '''查看喜欢过我的人'''
    pass