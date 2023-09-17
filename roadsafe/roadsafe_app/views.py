from django.shortcuts import render


def home(request):
    return render (request,'home.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')

def service(request):
    return render (request,'service.html')

def test(request):
    return render (request,'test.html')

def test2(request):
    return render (request,'test2.html')

def eld(request):
    return render (request,'eld.html')

def logistics(request):
    return render (request,'logistics.html')

def guide(request):
    return render (request,'guide.html')

def readmore(request):
    return render (request,'readmore.html')
