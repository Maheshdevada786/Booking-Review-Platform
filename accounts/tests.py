from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RedirectsTestCase(TestCase):
	def test_signup_redirects_to_login(self):
		"""POSTing valid signup data should redirect to the login page."""
		url = reverse('accounts:signup')
		data = {
			'username': 'testuser',
			'email': 'test@example.com',
			'password': 's3cretpass',
			'confirm_password': 's3cretpass',
		}
		response = self.client.post(url, data)
		# Expect a redirect (302) to accounts:login
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('accounts:login'))

	def test_login_redirects_to_home(self):
		"""Logging in should redirect to the myapp home page (LOGIN_REDIRECT_URL)."""
		# create user
		user = User.objects.create_user(username='joe', email='joe@example.com', password='pass1234')
		login_url = reverse('accounts:login')
		data = {
			'username': 'joe',
			'password': 'pass1234',
		}
		response = self.client.post(login_url, data)
		# LoginView should redirect to LOGIN_REDIRECT_URL (myapp:home)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('myapp:home'))
