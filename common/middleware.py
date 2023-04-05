from django.utils.deprecation import MiddlewareMixin

from common import errors
from lib.http import render_json
from user.models import User
class AuthMiddleware(MiddlewareMixin):
    white_list = [
        '/api/user/vcode/',
        '/api/user/login/',
        '/api/user/del/',
        '/api/user/logint/',
    ]
    def process_request(self,request):
        # 检查当前 path 是否在白名单
        if request.path in self.white_list:
            return
        # 用户登录验证
        uid = request.session.get('uid')
        if uid is None:
            return render_json(None,errors.LOGIN_REQUIRE)
        else:
            try:
                user = User.objects.get(id=uid)
            except User.DoesNotExist:
                return render_json(None,errors.USER_NOT_EXIST)
            else:
                # 将user 对象添加到request
                request.user = user

