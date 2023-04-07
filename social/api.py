from lib.http import render_json

from social import logic
from user.models import User
from social.models import Swiped
# Create your views here.
def get_rcmd_users(request):
    '''获取推荐列表'''
    user = request.user
    page = int(request.GET.get('page', 1)) # 页码
    per_page = 10 # 每页显示的数量
    start = (page - 1) * per_page # 每页显示的数量的开头一个
    end = start + per_page # 每页显示的数量的最后一个
    users = logic.rcmd_users(user)[start:end] # 匹配的所有用户
    result = [u.to_dict() for u in users]
    return render_json(result)

def like(request):
    '''喜欢'''
    sid = int(request.POST.get('sid'))
    is_matched = logic.like_someone(user,sid) # 检查两个人是否已经完成了匹配
    return render_json({'is_matched':is_matched})

def superlike(request):
    '''超级喜欢'''
    sid = int(request.POST.get('sid'))
    is_matched = logic.lsuperike_someone(user,sid) # 检查两个人是否已经完成了匹配
    return render_json({'is_matched':is_matched})

def dislike(request):
    '''不喜欢'''
    sid = int(request.POST.get('sid'))
    Swiped.dislike(user.id,sid)
    return render_json(None)

def rewind(request):
    '''反悔'''
    logic.rewind(request.user)
    return render_json(None)

def show_liked_me(request):
    '''查看喜欢过我的人'''
    users = logic.user_liked_me(request.user)
    result = [u.to_dict() for u in users]
    return render_json(result)
