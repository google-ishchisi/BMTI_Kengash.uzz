from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),

	path('detail/<int:id>/', detail, name='detail'),
	path('register/', register, name='register'),
	path('login/', login_user, name='login'),
	path('logout/', logout_user, name='logout'),
	
]	