from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Hood
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login/')
def home(request):
   posts = Post.objects.all()
   return render(request,'hood/home.html', {'posts': posts})

@login_required(login_url='/login/')
def profile(request):
   user = request.user
   hood = user.hood_set.first()
   return render(request, 'users/profile.html', {'hood':hood})

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

class PostDetailView(DetailView):
   model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['title', 'content']

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)