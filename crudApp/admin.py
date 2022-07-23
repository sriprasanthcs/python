from django.contrib import admin
from crudApp.models import crudapp

# Register your models here.
class crudadmin(admin.ModelAdmin):
    crud_details = ['sno','sname','semail']

admin.site.register(crudapp,crudadmin)