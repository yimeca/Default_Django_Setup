from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_url_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_uses_correct_template(self):
        self.assertTemplateUsed(self.response, "home.html")
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "<h1>Home</h1>")
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
    
    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)