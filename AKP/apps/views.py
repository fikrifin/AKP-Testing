from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.

def employee_list(request):
    context = {'employee_list' : Employees.objects.all(), 'position_list' : Position.objects.all(), 'division_list' : Division.objects.all()}
    return render(request, "apps/list.html", context)

def employee_form(request, employeesId=0):
    if request.method == "GET":
        if employeesId==0:
            form = EmployeeForm()
        else:
            employee = Employees.objects.get(pk=employeesId)
            form = EmployeeForm(instance=employee)
        return render(request, "apps/employee_form.html", {'form':form})
    else:
        if employeesId == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employees.objects.get(pk=employeesId)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect("/employee/list")

def employee_delete(request, employeesId=0):
    employee = Employees.objects.get(pk=employeesId)
    employee.delete()
    return redirect("/employee/list")

def position_form(request, positionId=0):
    if request.method == "GET":
        if positionId==0:
            form1 = PositionForm()
        else:
            position = Position.objects.get(pk=positionId)
            form1 = PositionForm(instance=position)
        return render(request, "apps/position_form.html", {'form1':form1})
    else:
        if positionId == 0:
            form1 = PositionForm(request.POST)
        else:
            position = Position.objects.get(pk=positionId)
            form1 = PositionForm(request.POST,instance=position)
        if form1.is_valid():
            form1.save()
        return redirect("/employee/list")
    
def position_delete(request, positionId=0):
    position = Position.objects.get(pk=positionId)
    position.delete()
    return redirect("/employee/list")

def division_form(request, divisionId=0):
    if request.method == "GET":
        if divisionId==0:
            form2 = DivisionForm()
        else:
            division = Division.objects.get(pk=divisionId)
            form2 = DivisionForm(instance=division)
        return render(request, "apps/division_form.html", {'form2':form2})
    else:
        if divisionId == 0:
            form2 = DivisionForm(request.POST)
        else:
            division = Division.objects.get(pk=divisionId)
            form2 = DivisionForm(request.POST,instance=division)
        if form2.is_valid():
            form2.save()
        return redirect("/employee/list")
    
def division_delete(request, divisionId=0):
    division = Division.objects.get(pk=divisionId)
    division.delete()
    return redirect("/employee/list")