from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Upload
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

class RegistrationView(CreateView):
	""" Custom Django user model and CreationForm used."""
	model = User
	form_class = UserCreationForm
	template_name = 'register.html'
	success_url = 'login'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/home/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = {
			'private_file': Upload.objects.filter(user=self.request.user),
			'public_file': Upload.objects.filter(private=False),
		}
		return context


class UploadView(CreateView):
	""" 
	Only need to specify the field names with CreatView, form generted automatically. 
	If a custom form is needed it must be specified by 'form_class' attribute, and form must be 
	created in forms.py and imported.
	"""
	model = Upload
	fields = ('private', 'file')
	template_name = 'upload_form.html'
	success_url = '/home/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.save()
		return super().form_valid(form) 



