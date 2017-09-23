from django.contrib.auth.views import *
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages



from .forms import RegisterForm
from .models import User


def _get_login_redirect_url(request, redirect_to):
    # Ensure the user-originating redirection URL is safe.
    if not is_safe_url(url=redirect_to, host=request.get_host()):
        return resolve_url(settings.LOGIN_REDIRECT_URL)
    return redirect_to


# Create your views here.
@deprecate_current_app
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='home/home_page.html',
          redirect_field_name='next',
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=False):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if redirect_authenticated_user and request.user.is_authenticated:
        redirect_to = _get_login_redirect_url(request, redirect_to)
        if redirect_to == request.path:
            raise ValueError(
                "Redirection loop for authenticated user detected. Check that "
                "your LOGIN_REDIRECT_URL doesn't point to a login page."
            )
        return HttpResponseRedirect(redirect_to)
    elif request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return HttpResponseRedirect(_get_login_redirect_url(request, redirect_to))
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    messages.error(request, '登录验证失败', extra_tags='bg-warning text-warning')

    return HttpResponseRedirect(_get_login_redirect_url(request, redirect_to))

def register(request):
    if request.is_ajax():
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = User()
            user.username = register_form.cleaned_data['username']
            user.email = register_form.cleaned_data['email']
            user.password = make_password(register_form.cleaned_data['password'])
            user.save()
            return JsonResponse({'status': 'success'})
        else:
            data = dict()
            status = {'status': 'fail'}
            data['errors'] = register_form.errors
            data.update(status)
            return JsonResponse(data)
    else:
        return HttpResponse('Sever Error Or Your JavaScript is closed, please turn on your Js and try to register later')
