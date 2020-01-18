from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import UserRegisterForm

# Create your views here.
def home(request):
   return render(request,'hood/home.html')

def profile(request):
   return render(request, 'profile/profile.html')

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Your account has been created! You are now able to log in')
         return redirect('login')
   else:
      form = UserRegisterForm()
   return render(request, 'users/register.html', {'form': form})

class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['title', 'content']

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)