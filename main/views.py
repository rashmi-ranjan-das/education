from django.shortcuts import render
from .models import Books, Python, Cplusplus, MLAI
# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def explore(request): 
    return render(request, 'main/explore.html')

def resources(request):
    pythons = Python.objects.all()
    cplusplus = Cplusplus.objects.all()
    mlai = MLAI.objects.all()
    return render(request, 'main/resources.html', {'pythons':pythons, 'cplusplus': cplusplus, 'mlai':mlai})

def articles(request): 
    return render(request, 'main/articles.html')

def team(request):
    return render(request, 'main/team.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def pi1001(request):
    return render(request, 'main/Articles/Python/1001.html')

def pi1002(request):
    return render(request, 'main/Articles/Python/1002.html')

def pi1003(request):
    return render(request, 'main/Articles/Python/1003.html')

def ci1001(request):
    return render(request, 'main/Articles/C++/1001.html')

def ci1002(request):
    return render(request, 'main/Articles/C++/1002.html')

def ci1003(request):
    return render(request, 'main/Articles/C++/1003.html')

def mli1001(request):
    return render(request, 'main/Articles/MLAI/1001.html')

def mli1002(request):
    return render(request, 'main/Articles/MLAI/1002.html')

def mli1003(request):
    return render(request, 'main/Articles/MLAI/1003.html')

def webi1001(request):
    return render(request, 'main/Articles/WebDev/1001.html')

def webi1002(request):
    return render(request, 'main/Articles/WebDev/1002.html')

def webi1003(request):
    return render(request, 'main/Articles/WebDev/1003.html')