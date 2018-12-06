from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, HomeView, UploadView
from django.contrib.auth.views import login

urlpatterns = [
	path('', RegistrationView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('home/', HomeView.as_view(), name='home'),
	path('upload/', UploadView.as_view(), name='upload'),
]