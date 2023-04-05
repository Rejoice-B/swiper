broker_url = 'redis://:redisblj@192.168.134.130:6379/0'
broker_pool_limit = 1000  # Borker 连接池，默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle','json']

task_serializer = 'pickle' # pickle 速度比Python快

result_backend = 'redis://:redisblj@192.168.134.130:6379/0'
result_serializer='pickle'

result_cache_max=10000 #任务结果的最大缓存数量
result_expires = 3600#任务结果过期时间


worker_redirect_stdouts_level='INFO'#日志的级别，日志输出的参数
