from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@api_view(['POST'])
@csrf_exempt
def sample_post(request):
    print(request.data)
    return JsonResponse({'status': True})


@api_view(['GET'])
@csrf_exempt
def sample_get(request):
    print(request.data)
    return JsonResponse({'status': True})