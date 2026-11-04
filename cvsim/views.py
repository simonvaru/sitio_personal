from django.shortcuts import render


def cvsim(request):
    return render(request, 'cvsim/cvsim.html', {})
