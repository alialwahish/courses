from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Course, Describtion
def index(request):
    print(Course.objects.first())
    context={'courses' : Course.objects.all(),
    'descs':Describtion.objects.all()}
    return render(request,'appCourses/index.html',context)

def add(request):
    print("in adding")
    if request.method=='POST':
        print("in IF ")
        print('request.POST')
        Course.objects.register(request)
        return redirect('/')
    else:     
        return redirect('/')
   
def distroy(request,id):
    print("trying to delete",Course.objects.get(id=id).name)
    Course.objects.get(id=id).delete()
    return redirect('/')

def confRem(request,id):
    print("confirm delete",id)
    
    return render(request,'appCourses/confDel.html',{'course' : Course.objects.get(id=id)})
    