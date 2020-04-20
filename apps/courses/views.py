from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 
    return render(request, 'courses/index.html') 


def newCourse(request):

    errors = Course.objects.validator(request.POST)

    duplicate = Course.objects.duplicate_validator(request.POST)

    if len(duplicate) > 0:
        messages.error(request, duplicate)
        return redirect('/')

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request,v)
        return redirect('/')
    else:
        messages.success(request, "Course added!")
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')


def destroyCourse(request, id):
    pass


