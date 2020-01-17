from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
   path('', views.home, name ='hood-home'),
   path('accounts/', include('registration.backends.simple.urls')),
   path('login/', LoginView.as_view(template_name= '/'), name='user_login'),
   path('logout/', LogoutView.as_view(template_name='/'), name="user_logout"),
]