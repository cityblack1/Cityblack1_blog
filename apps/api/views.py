from django.http.response import JsonResponse

from users.models import User


def check_from_db(name, field='username'):
    if name:
        kw = {field: name}
        if User.objects.filter(**kw):
            return True
    return False


def check_username(request):
    if request.is_ajax():
        username = request.GET.get('username', '')
        if not check_from_db(username):
             return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'})


def check_email(request):
    if request.is_ajax():
        email = request.GET.get('email', '')
        if not check_from_db(email, 'email'):
             return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'})


