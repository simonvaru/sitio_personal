from django.shortcuts import render


def demoapp3(request):
    return render(request, 'demoapp3/demoapp3.html')
