from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *

class DateInput(forms.DateInput):
    input_type = "date"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('position','name','birth_date','phone_number','gender','join_date')
        labels = {
            'position' : 'Posisi',
            'name':'Nama Lengkap',
            'birth_date' : 'Tanggal Lahir',
            'phone_number' : 'Nomor HP',
            'gender' : 'Jenis Kelamin',
            'join_date' : 'Tanggal Mendaftar'
        }
        widgets = {
            'birth_date': DateInput(),
            'join_date': DateInput()
        }

    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ('devision', 'posisitionName')
        labels = {
            'devision' : 'Bagian Divisi',
            'posisitionName' : 'Nama Posisi'
        }
    
    def __init__(self, *args, **kwargs):
        super(PositionForm,self).__init__(*args, **kwargs)
        self.fields['devision'].empty_label = "Select"

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ('divisionName',)
        labels = {
            'divisionName' : 'Nama Divisi',
        }