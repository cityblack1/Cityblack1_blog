from blog.models import BlogPage
from django.contrib import messages

from .forms import MyCommentForm, ContactForm

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_protect
from django_comments.models import CommentFlag


from django_comments.views.utils import next_redirect

from django_comments_xtd import (get_model as get_comment_model)
from django_comments_xtd.conf import settings
from django_comments_xtd.models import (LIKEDIT_FLAG, DISLIKEDIT_FLAG)
from django_comments_xtd.utils import send_mail, has_app_model_option

# Create your views here.


def comment_view(request, slug):
    try:
        blog = BlogPage.objects.get(slug=slug)
        url = blog.get_url()
        if request.method == 'POST':
            comment_forms = MyCommentForm(request.POST)
            if comment_forms.is_valid():
                comment = comment_forms.save(commit=False)
                comment.blog = blog
                comment.save()
                return redirect(url)
            else:
                render(request, 'blog/blog_page.html', context={'comment_forms': comment_forms})
        return redirect(url)
    except:
        return redirect('/')


STAT = 0


def contact_view(request):
    global STAT
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            STAT = 1
            return redirect(request.path)
        else:
            return render(request, 'blog/contact_page.html', {'contact_form': contact_form, 'message': None})

    if request.method == 'GET':
        if STAT:
            STAT = 0
            return render(request, 'blog/contact_page.html', {'message': '1'})
        return render(request, 'blog/contact_page.html', {'message': None})

    else:
        return redirect('/')


def perform_like(request, comment):
    """Actually set the 'Likedit' flag on a comment from a request."""
    flag, created = CommentFlag.objects.get_or_create(comment=comment,
                                                      user=request.user,
                                                      flag=LIKEDIT_FLAG)
    if created:
        CommentFlag.objects.filter(comment=comment,
                                   user=request.user,
                                   flag=DISLIKEDIT_FLAG).delete()
    else:
        flag.delete()
    return created



@csrf_protect
def like(request, comment_id, next=None):
    """
    Like a comment. Confirmation on GET, action on POST.

    Templates: :template:`django_comments_xtd/like.html`,
    Context:
        comment
            the flagged `comments.comment` object
    """

    comment = get_object_or_404(get_comment_model(), pk=comment_id,
                                    site__pk=settings.SITE_ID)
    next = comment.get_absolute_url()
    if request.user.is_authenticated():
        if not has_app_model_option(comment)['allow_feedback']:
            ctype = ContentType.objects.get_for_model(comment.content_object)
            raise Http404("Comments posted to instances of '%s.%s' are not "
                          "explicitly allowed to receive 'liked it' flags. "
                          "Check the COMMENTS_XTD_APP_MODEL_OPTIONS "
                          "setting." % (ctype.app_label, ctype.model))

        perform_like(request, comment)
        return next_redirect(request,
                             fallback=next or 'comments-xtd-like-done',
                             c=comment.pk)
    messages.error(request, '只有登录用户才能点赞, 请在侧边栏内登录再尝试点赞！', extra_tags='bg-warning text-warning')
    return next_redirect(request,
                         fallback=next or 'comments-xtd-like-done',
                         c=comment.pk)
