from django.contrib import admin
from . import models
from .models import student_data,student_school_data

# Register your models here.
class student_dataAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name']

admin.site.register(models.student_data,student_dataAdmin)


class student_school_dataAdmin(admin.ModelAdmin):
    list_display=['id','student','c_class','Percentage','Commute']

admin.site.register(models.student_school_data,student_school_dataAdmin)