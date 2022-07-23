from django.shortcuts import render,redirect
from django.conf import settings
from .models import crudapp
# from crudApp.models import crudapp
from crudApp.forms import crudformadd

# Create your views here.
def crudview(request):
    crudDetail = crudapp.objects.all()
    return render(request, 'crudApp/sample.html', {'crudDetail' : crudDetail})

def crudinsert(request):
    form = crudformadd()
    if request.method == 'POST':
        form = crudformadd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cruddetail')
    return render(request, 'crudApp/createform.html', {'form' : form})

def cruddelete(request,id):
   crudDelete = crudapp.objects.get(id=id)
   crudDelete.delete()
   return redirect('/cruddetail')

def crudupdate(request,id):
    crudUpdate = crudapp.objects.get(id=id)
    if request.method == 'POST':
            form = crudformadd(request.POST,instance=crudUpdate)
            if form.is_valid():
                form.save()
                return redirect('/cruddetail')
    return render(request, 'crudApp/updateform.html', {'crudUpdate' : crudUpdate})
   
