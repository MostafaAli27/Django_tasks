from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from students.models import Student

from .forms import Student_form
# Create your views here.

def Hello(request):
    template = loader.get_template('show.html')
    return HttpResponse(template.render())

def list_view(request):
    context = {}
    context["dataset"] = Student.objects.all()
    return render(request,"list_view.html",context)

def cv(request):
    content = loader.get_template('cv.html')
    return HttpResponse(content.render())

def add_student(request):
  if request.method == "POST":
    form = Student_form(request.POST)
    
    if form.is_valid():
       form.save()
       return redirect('/list')  
    
  else:
      form = Student_form()
      
  
  return render(request, 'add_student.html', {'form': form})