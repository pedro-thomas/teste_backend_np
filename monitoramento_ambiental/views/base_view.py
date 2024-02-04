from django.shortcuts import render

def base_page(request):
    return render(request, 'base/base.html')
