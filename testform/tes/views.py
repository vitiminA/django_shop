from django.shortcuts import render
from django.http import HttpResponse
from .forms import smart_Form
from .models import smartForm

# Create your views here.
def smart(request):
    sm = smart_Form()
    return render(request, 'tes/smart.html', {'sm':sm})

def savesmart(request):
    if request.method =='POST':
        sm = smart_Form(request.POST,request.FILES)
        if sm.is_valid():
            saveSM = smartForm(title = sm.cleaned_data['title'],
                               image = sm.cleaned_data['image'],
                               body = sm.cleaned_data['body'])
            saveSM.save()
            return HttpResponse('save success')
        else:
            return HttpResponse("not va_lid")
    else:
        return HttpResponse('not POST')