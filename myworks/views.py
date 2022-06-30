from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index2.html')

def analyze(request):
    jj = request.POST.get('text')
    ss = jj
    uu = request.POST.get('SmallAlpha')
    vv = request.POST.get('FullCaps')
    if uu == 'on':
        ss = ''.join(filter(str.isalpha, ss))
    if vv == 'on':
        ss = ss.upper()
    stuff = {'txt': ss}
    return render(request, 'analyze.html', stuff)


