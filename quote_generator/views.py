from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'quote_generator/index.html')

#def about(request):
#    return render(request, 'quote_generator/about.html')