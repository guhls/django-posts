from django.test import TestCase
from django.urls import resolve, reverse
from posts import views


class TestBot(TestCase):
    def test_check_url_bot(self):
        url = reverse('posts:bot')
        self.assertEqual(url, '/posts/bot/')

    def test_check_view_bot(self):
        response = resolve(reverse('posts:bot'))
        self.assertIs(response.func, views.bot)
