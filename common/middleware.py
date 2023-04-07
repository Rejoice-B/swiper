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
            return render_json(None,errors.LoginRequire.code)
        else:
            try:
                user = User.objects.get(id=uid)
            except User.DoesNotExist:
                return render_json(None,errors.UserNotExist.code)
            else:
                # 将user 对象添加到request
                request.user = user

class LogicErrorMiddleware(MiddlewareMixin):
    def process_exception(self,request,exception):
        '''异常处理'''
        if isinstance(exception, errors.LogicError): # 判断抛出的异常类型是否是errors.LogicError,这里的exception是异常产生的一个实例
            return render_json(None,exception.code) # 处理逻辑错误
        # else:
        #     #处理程序错误
        #     error_info = format_exception(*exc_info())
        #     err_log.error(''.join(error_info)) # 将异常信息输出到错误日志
        #     return render_json(error=errors.InternalError) # 程序错误统一用 InternalError
