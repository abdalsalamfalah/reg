from django.shortcuts import render,redirect
from salam import models
from salam import forms
from django.contrib import messages
# Create your views here.
def Index(request):
    information=models.info.objects.all()# من هنا نحدد جميع البيانات لعرضها
    context={'information':information}
    return render(request,'index.html',context)


def inserting(request):
    infor=models.info.objects.all()#
    form_data=forms.inforeg(request.POST or None)
    if form_data.is_valid():
        regform=models.info()
        regform.full_name=form_data.cleaned_data['Full_name']
        regform.the_age=form_data.cleaned_data['The_age']
        regform.phone_number=form_data.cleaned_data['Phone_num']
        regform.save()
        messages.success(request,f'احسنت  {regform.full_name} تم حجزك بنجاح رقم حجزك هو ')
        return redirect('regform')


    context={
        'formregister':form_data,
        'infor':infor
        }

    return render(request,'regform.html',context)

def Delete(request, item_id):
    dels =models.info.objects.get(pk=item_id)
    if request.method=='POST':
        dels.delete()
        messages.success(request,f'احسنت  تم الحذف بنجاح ')
        return redirect('index')
  
    return render(request,'Delete.html')



def Update(request, item_id):
    item=models.info.objects.get(pk=item_id)
    form=forms.updateinfo(instance=item)
    if request.method=='POST':
        form=forms.updateinfo(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={
        'form':form
        }
    return render(request,'update.html',context)



def Me(request):
    return render(request,'me.html')

        
        
    