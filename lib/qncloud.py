from urllib.parse import urljoin
from qiniu import Auth, put_file, etag
from swiper import config
from worker import call_by_worker
QN_Auth = Auth(config.QN_ACCESS_KEY,config.QN_SECRET_KEY)

def get_qn_url(filename):
    '''获取文件URL'''
    return urljoin(config.QN_BASE_URL, filename) # 拼接


def upload_to_qiniu(localfile, key):
    '''
    将本地文件上传到七牛云

    Args:
        localfile: 本地文件位置
        key: 上传到服务器后的文件名
    '''
    # #构建鉴权对象
    # q = Auth(access_key, secret_key)
    # #要上传的空间
    # bucket_name = 'Bucket_Name'
    # #上传后保存的文件名
    # key = 'my-python-logo.png'
    #生成上传 Token，可以指定过期时间等
    token = QN_Auth.upload_token(config.QN_BUCKET, key, 3600)
    #要上传文件的本地路径
    ret, info = put_file(token, key, localfile, version='v2')

    assert ret['key'] == key # assert 判断是否正常，是就继续，否则停止运行
    assert ret['hash'] == etag(localfile)
    url= get_qn_url(key)

    return ret,info,url

'''定义了async_upload_to_qiniu为一个异步的upload_to_qiniu函数，相当于有两个upload_to_qiniu函数，一个异步，一个不是异步'''
async_upload_to_qiniu = call_by_worker(upload_to_qiniu)