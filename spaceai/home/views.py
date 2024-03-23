from django.shortcuts import render
from compression_middleware.decorators import compress_page
from django.views.decorators.cache import cache_page


# Create your views here.
@compress_page
@cache_page(60 * 5) 
def home(request):
    context = {}
    return render(request,'pages/home.html',context=context)