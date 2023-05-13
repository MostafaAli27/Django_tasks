from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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
