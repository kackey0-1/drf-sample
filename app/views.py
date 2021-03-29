from health_check.views import MainView
from django.http import JsonResponse
from django.http import response


class HealthCheckCustomView(MainView):

    def get(self, request, *args, **kwargs):
        status_code = 200
        content = {'status': 'UP'}
        return JsonResponse(data=content, status=status_code)


