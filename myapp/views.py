from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl
from .models import Service

# Create your views here.
def index(req):
    return render(req,'myapp/index.html')
    # if req.method == 'POST':
    #     post = req.POST
    #     s = Service()
    #     s.icon = post['icon']
    #     s.title = post['title']
    #     s.detail = post['detail']
    #     s.save()
    #     services = Service.objects.all()
    #     print(services)
    #     return render(req, 'myapp/index.html', { 'services': services })
    # else:
    #     print('ร้องขอทำมะดา')
    #     services = Service.objects.all()
    #     print(services)
    #     return render(req, 'myapp/index.html', { 'services': services })

def Developer(req):
    return render(req,'myapp/Developer.html')

def comsci(req):
    return render(req,'myapp/comsci.html')

def Memo(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/Memo.html', { 'services': services })
    else:
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/Memo.html', { 'services': services })


