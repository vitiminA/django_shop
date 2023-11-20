# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import postModel
# from .forms import post_Model
# # Create your views here.
# def index(request):
#     # pm =  postModel.objects.all()
#     pm =  postModel.objects.all()
#     return render(request, 'shop1/index.html', {'pm':pm})

# def index1(request):
#     if request.method =="POST":
#         pm = post_Model(request.POST,request.FILES)
#         if pm.is_valid():
#             pm.save()
#             return redirect('index:index')
#     else: 
#         return HttpResponse("not POST")
    
# def index2(request):
#     # pm =  postModel.objects.all()
#     pm =  post_Model
#     return render(request, 'shop1/index1.html', {'pn':pm})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import postModel
from .forms import post_Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    template_name = 'shop1/index.html'
    # def get_template_names(self):
    #     return ['shop1/index.html', 'shop1/ad_product.html']

    def get(self, request):
        pm = postModel.objects.all()
        return render(request, self.template_name, {'pm': pm})

class Index1View(LoginRequiredMixin, View):
    template_name = 'shop1/index1.html'

    def get(self, request):
        pm = post_Model()
        return render(request, self.template_name, {'pn': pm})

    login_url = '/login/'
    def post(self, request):
        pm = post_Model(request.POST, request.FILES)
        if pm.is_valid():
            pm.save()
            return redirect('/ad_product/')
        else:
            return HttpResponse("not POST")

#Đường dẫn bình thường khi không đăng nhập vẫn có thể dùng đường dẫn để xem
# def get_template_names(request):
#         pm = postModel.objects.all()
#         # pm = postModel.objects.get(id = id)
#         return render(request, 'shop1/ad_product.html', {'pm': pm})


#Xử lý khi đăng nhập mới có thể vào trang ad_product
class Get_template_names(LoginRequiredMixin, View):
    login_url='/login/'

    def get(self, request):
        pm = postModel.objects.all()
        return render(request, 'shop1/ad_product.html', {'pm': pm})

