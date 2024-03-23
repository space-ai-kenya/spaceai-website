from django.shortcuts import render
from compression_middleware.decorators import compress_page

# Create your views here.
@compress_page
def home(request):
    context = {}
    return render(request,'pages/home.html',context=context)