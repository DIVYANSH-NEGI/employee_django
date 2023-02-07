from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



def index(request):

    length = len(Employee.objects.all())
    employee_list = Employee.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(employee_list, 10)

    try:
        employee = paginator.page(page)
    except PageNotAnInteger:
        employee = paginator.page(1)
    except EmptyPage:
        employee = paginator.page(paginator.num_pages)


    context={
             'employee':employee,
             'length':length,
    }
    return render(request,'index.html',context)





def add(request):
    context ={}

    return render(request,'add.html',context)

def addrecord(request):
  name = request.POST['name']
  address = request.POST['address']
  email = request.POST['email']
  position = request.POST['position']
  company = request.POST['Company_id']
  employee = Employee(name=name,address=address,email=email,position=position,Company_id_id=company)
  employee.save()
  return redirect('/')


def delete(request, id):
  employee = Employee.objects.get(Emp_id=id)
  employee.delete()
  return redirect('/')

def update(request, id):
  employee = Employee.objects.get(Emp_id=id)

  context = {
    'employee': employee,
  }
  return render(request,'update.html',context)




def updaterecord(request, id):

  name = request.POST['name']
  address = request.POST['address']
  email = request.POST['email']
  position = request.POST['position']
  company = request.POST['Company_id']

  employee = Employee.objects.get(Emp_id=id)

  employee.name = name
  employee.address = address
  employee.email = email
  employee.position = position
  employee.Company_id_id = company
  employee.save()
  return redirect('/')
