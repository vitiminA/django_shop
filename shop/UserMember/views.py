from django.shortcuts import render, redirect
from .forms import registerForm, loginForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import time
# Create your views here.

class registerUser(View):
    def get(self, request):
        rF = registerForm 
        return render(request, 'UserMember/register.html', {'rF':rF})
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('You have successfully created an account')
    
class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'UserMember/login.html', {'lF':lF})
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            # return render(request, 'shop1/ad_product.html')
            return redirect('/')
        else:
            return HttpResponse('login faild')


def logoutUser(request):
    logout(request)
    time.sleep(1)
    return redirect('/')


class privatePage(LoginRequiredMixin, View):
    login_url='/login/'

    def get(self, request):
        return render(request, 'UserMember/private.html')
    