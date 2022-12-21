import os
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from .models import Posts, User
from .utils.request_img import get_img

load_dotenv()


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


client = Client(
    os.environ.get('account_sid'),
    os.environ.get('auth_token')
)


@ csrf_exempt
def bot(request):
    msg_text = request.POST.get('Body')
    number = request.POST.get('From')
    name = request.POST.get('ProfileName')
    media = request.POST.get('MediaUrl0')

    resp = MessagingResponse()
    msg = resp.message()

    print(request.POST)

    if msg_text == 'oi':
        msg.body(f"Olá {name}, O Bot está funcionando")
        return HttpResponse(resp)

    if media:
        just_number = number.replace('whatsapp:+', '')
        filename = f'{just_number}.jpg'
        image_file = get_img(media, filename)

        if image_file:
            gustavo = User.objects.get(username="gustavo")

            post = Posts.objects.create(  # noqa: F841
                nome=gustavo,
                number=number.replace('whatsapp:+', ''),
                cover=image_file,
            )

            msg.body(f'Thank you, Image posted! with id {post.pk}')
        else:
            msg.body('Something gones wrong')

    return HttpResponse(resp)
