from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def members(request):
    mymembers = Members.objects.all()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers':mymembers,
    }
    return render(request, 'myfirst.html', context)

def all_members(request):
    mymembers = Members.objects.all()
    context={
        'mymembers': mymembers,
    }
    for x in mymembers:
        print(x.firstname, x.lastname, x.age)
    return render(request, 'all_members.html', context)