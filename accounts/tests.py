from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        test_user = User.objects.create_user(
            username="test_user", email="test_user@email.com", password="test_user_password123"
        )
        self.assertEqual(test_user.username, "test_user")
        self.assertEqual(test_user.email, "test_user@email.com")
        self.assertEqual(test_user.check_password("test_user_password123"), True)
        self.assertTrue(test_user.is_active)
        self.assertFalse(test_user.is_staff)
        self.assertFalse(test_user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        test_admin_user = User.objects.create_superuser(
            username="test_admin_user", email="test_admin_user@email.com",
            password="test_admin_user_password123"
        )
        self.assertEqual(test_admin_user.username, "test_admin_user")
        self.assertEqual(test_admin_user.email, "test_admin_user@email.com")
        self.assertEqual(test_admin_user.check_password("test_admin_user_password123"), True)
        self.assertTrue(test_admin_user.is_active)
        self.assertTrue(test_admin_user.is_staff)
        self.assertTrue(test_admin_user.is_superuser)

class SignupPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)