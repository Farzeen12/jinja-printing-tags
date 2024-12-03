from django.shortcuts import render

# Create your views here.

def car(request):
    d={'name':'M5','power':'770 BHP'}
    return render(request,'car.html',context=d)