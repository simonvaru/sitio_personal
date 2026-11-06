from django.shortcuts import render


def demoapp2(request):
    return render(request, 'demoapp2/demoapp2.html')
