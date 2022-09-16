from django.test import TestCase
from django.urls import resolve, reverse

from . import views

# Create your tests here.


class TestPosts(TestCase):
    def test_check_url_posts(self):
        url = reverse('posts:home')
        self.assertEqual(url, '/posts/')

    def test_check_view_posts(self):
        view = resolve(reverse('posts:home')).func
        self.assertIs(view, views.home)

    def test_check_template_posts(self):
        response = self.client.get(reverse('posts:home'))
        self.assertTemplateUsed(response, 'posts/pages/home.html')
