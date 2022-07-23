from django import forms
from crudApp.models import crudapp

# Create your models here.
class crudformadd(forms.ModelForm):
    class Meta:
        model = crudapp
        fields = '__all__'
