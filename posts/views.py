import random

from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from utils.secret_manager import get_s3_config, get_secrets

from .models import Posts, User
from .utils.request_img import get_img


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


bucket = get_s3_config()['s3']['bucket']
key = get_s3_config()['s3']['key']


account_sid = get_secrets(bucket=bucket, key=key)
auth_token = get_secrets(bucket=bucket, key=key)
client = Client(account_sid, auth_token)


@ csrf_exempt
def bot(request):
    msg_text = request.POST.get('Body')
    number = request.POST.get('From')
    name = request.POST.get('ProfileName')
    media = request.POST.get('MediaUrl0')

    resp = MessagingResponse()

    print(request.POST)

    if msg_text == 'oi':
        resp.message(f"Olá {name}, O Bot está funcionando")

    if media:
        just_number = number.replace('whatsapp:+', '')
        filename = f'{just_number}.jpg'
        media_url = get_img(media, filename)

        post = Posts.objects.create(
            nome=User.objects.create_user(username='gustavo3'),
            number=number.replace('whatsapp:+', ''),
            cover=File(open(media_url, 'rb')),
        )

    return HttpResponse('ola')
