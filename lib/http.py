import json

from django.conf import settings
from django.http import HttpResponse, JsonResponse

def render_json(data,code=0):#用户返回的data转化封装，code是状态码
    result = {
        'data': data,
        'code': code
    }
    if settings.DEBUG:
        json_str = json.dumps(result, ensure_ascii=False, indent=4,sort_keys=True)
    else:
        json_str = json.dumps(result, separators=[',', ':'],ensure_ascii=False)
    return HttpResponse(json_str)