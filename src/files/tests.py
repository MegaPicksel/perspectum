from django.test import TestCase
from .models import Upload
from django.contrib.auth.models import User
from django.urls import reverse


class FilesTest(TestCase):
 
	def create_user(username='test', password='password'):
		""" 
		user field in Uplaod has a foreighkey relationship, thus we instatntiate User model first.
		Once a user is created, you need to either delete the user before running another test, 
		or change username,otherwise the NOT_NULL constraint will fail.
		"""
		return User.objects.create(username=username, password=password)

	user = create_user()   # Creating one user instance to use in all of the methods.

	def create_file(self, private=True, file='test.txt', user=user):
		return Upload.objects.create(private=private, file=file, user=user)

	def test_file_creation(self):
		""" Test Uplaod model, make sure it can be instantiated and create a model."""
		test = self.create_file()
		self.assertTrue(isinstance(test, Upload))

	def test_upload_view(self):
		""" Testing UploadView."""
		test = self.create_file()
		url = reverse('upload')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)

	def test_register_view(self):
		""" Testing RegistrationView."""
		test = self.user
		url = reverse('register')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
