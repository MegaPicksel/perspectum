from django.db import models
from django.contrib.auth.models import User

class Upload(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	private = models.BooleanField(default=True)
	file = models.FileField(upload_to='files/uploads')
	user = models.ForeignKey(User, on_delete=models.CASCADE,)

	def __str__(self):
		return self.file
