from django.shortcuts import render

def main_page(request):
    return render(request, 'main/main_page.html')


def about_us(request):
    return render(request, 'main/about_us.html')

def servises(request):
    return render(request, 'main/services.html')


