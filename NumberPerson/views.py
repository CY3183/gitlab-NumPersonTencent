from django.http import JsonResponse
from rest_framework.views import APIView
from NumberPerson import tencent_chat


class DataView(APIView):
    def get(self, request):
        text = request.GET.get('text')
        if text:
            info = tencent_chat.tencent_chat(text)
            if info:
                return JsonResponse({'code': 200, 'msg': 'success', 'data': info})
            return JsonResponse({'code': 200, 'msg': "腾讯接口没有返回数据，请重试！"})
        else:
            return JsonResponse({'code': 200, 'msg': '请传参数!'})

