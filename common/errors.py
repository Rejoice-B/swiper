'''定义页面验证码（错误类型）'''
OK = 0
VCODE_ERROR = 1000
LOGIN_REQUIRE = 1001
USER_NOT_EXIST = 1002
PROFILE_ERROR = 1003

'''
定义类的特殊方法
def fun(self):
    print('DOG')
Dog - type('Dog',(object,),{'head':1,'body':1,'leg':4,'tail':1,'run':run}} #(名称，继承的类，属性方法）
d = Dog()
'''
class LogicError(Exception):
    '''逻辑异常类'''
    code = 0
    def __str__(self):
        return self.__class__.__name__

def generate_login_error(name: str,code: int) -> LogicError:
    base_cls = (LogicError,)
    return type(name,base_cls,{'code':code})

Ok = generate_login_error('OK',0)
VcodeError = generate_login_error('VcodeError',1000)
VcodeExist = generate_login_error('VcodeExist',1001)
LoginRequire = generate_login_error('LoginRequire',1002)
UserNotExist = generate_login_error('UserNotExist',1003)
ProfileError = generate_login_error('ProfileError',1004)