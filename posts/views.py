import random

from django.shortcuts import render

from .models import Posts


def home(request):
    posts = Posts.objects.filter(is_published=False).order_by('-id')

    if posts:
        for post in posts:
            post.is_published = True
            post.save()

        new_photos = True
    else:
        posts = Posts.objects.all()

        lst_all_pks = []
        for post in posts:
            lst_all_pks.append(int(post.pk))

        try:
            lst = random.choices(lst_all_pks, k=5)
        except Exception:
            lst = []

        posts = Posts.objects.filter(pk__in=lst).order_by('-id')

        new_photos = False

    delay_img = 5000

    if new_photos:
        delay_img *= 2
        reload_page = (len(posts) * delay_img) * 2
    else:
        reload_page = (len(posts) * delay_img)

    return render(
        request,
        'posts/pages/home.html',
        context={
            'posts': posts,
            'range': range(len(posts)),
            'new_photos': new_photos,
            'reload_page': reload_page,
            'delay_img': delay_img,
        }
    )
