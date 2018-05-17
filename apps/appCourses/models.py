from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.contrib.messages import get_messages


class CourseManager(models.Manager):
    def register(self,request):
        if len(request.POST['name'])<5:
            messages.add_message(request,messages.ERROR,"Name can't be less than 5 letters")
            print("name Error")

        if len(request.POST['desc'])<15:
            messages.add_message(request,messages.ERROR,"Describtion can't be less than 15 letters")
            print("desc Error")
        if len(get_messages(request))>0:
            return False

        else:
            print("creating object")
            c1=Course(name=request.POST['name'])
            c1.save()
            d1=Describtion(course=c1,content=request.POST['desc'])
            d1.save()
            print("the describtion course",d1.course)
            print("the course describtion",c1.describtion.content)
           
        
             


class Course(models.Model):
    name = models.CharField(max_length = 255)
    created_at=models.DateTimeField(auto_now_add=True)
    objects=CourseManager()
    def __str__(self):
        return (self.name)


class Describtion(models.Model):
    course=models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    content=models.CharField(max_length =255)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.course.name)   
        


class joinCrsWithDescs(models.Model):
    describtion=models.ForeignKey(Describtion,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return  (self.name,self.describtion)








class Comments(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    coumments_course=models.ForeignKey(Course, on_delete=True,related_name='comments')
  
