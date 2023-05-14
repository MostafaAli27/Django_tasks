from django.urls import path

from . import views

urlpatterns =[
    path('Hello/',views.Hello,name='Hello'),
    path('list/',views.list_view,name='list'),
    path('cv/',views.cv,name='cv'),
    path('add_student/',views.add_student,name='add_student')
]