from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from blog.models import BlogPage, Comment


def send_html_email(to, subject, template_name, context, sender):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, to=[to])
    msg.content_subtype = "html"
    return msg.send()


def article_comment(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        user = User.objects.get(username=request.POST.get('user_name'))
        content = request.POST.get('comment')
        article = get_object_or_404(BlogPage, slug=slug)
        parent_comment = request.POST.get('parent_comment')
        comment_status = 'unsuccessful'

        if parent_comment and content:
            parent_comment = Comment.objects.get(id=parent_comment)
            comment = Comment.objects.create(article=article, user=user, content=content, parent_comment=parent_comment)
            comment.save()
            comment_status = 'success'
            context = { 'article': article, 'user': user, 'content': content }
            send_html_email(settings.COMMENT_ADMIN_EMAIL, 'Comment received for moderation', 'emails/comment_moderation.html', context, settings.DEFAULT_FROM_EMAIL)
        elif content:
            comment = Comment.objects.create(article=article, user=user, content=content)
            comment.save()
            comment_status = 'success'
            context = { 'article': article, 'user': user, 'content': content }
            send_html_email(settings.COMMENT_ADMIN_EMAIL, 'Comment received for moderation', 'emails/comment_moderation.html', context, settings.DEFAULT_FROM_EMAIL)
    else:
        raise Http404

    return redirect('/blog/'+slug+'?comment_status='+comment_status+'#anchor-comment-status')