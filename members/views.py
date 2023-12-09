from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Members

def members(request):
    mymembers = Members.objects.all()
    template = loader.get_template('members.html')
    context = {
        'mymembers':mymembers,
    }
    return render(request, 'members.html', context)

def all_members(request):
    mymembers = Members.objects.all()
    context={
        'mymembers': mymembers,
    }
    return render(request, 'all_members.html', context)

def details(request, id):
    mymembers = Members.objects.get(id=id)
    context = {
        'mymembers':mymembers,
    }
    return render(request, 'details.html', context)