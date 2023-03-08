from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
def frontend(request):
    return render(request, 'frontend.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')

def backend(request):
    return render(request, 'backend.html')