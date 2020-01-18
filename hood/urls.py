from django.urls import path, include
from . import views
from .views import PostCreateView, PostDetailView


urlpatterns = [
   path('', views.home, name ='hood-home'),
   path('profile/', views.profile, name='user-profile'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('post/new/', PostCreateView.as_view(), name='post-create'),
]