from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_add'),
    path('<int:employeesId>/', views.employee_form, name='employee_update'),
    path('delete/<int:employeesId>/', views.employee_delete, name='employee_delete'),
    path('list/', views.employee_list, name='index'),
    path('positionadd', views.position_form, name='position_add'),
    path('position/<int:positionId>/', views.position_form, name='position_update'),
    path('position/delete/<int:positionId>/', views.position_delete, name='position_delete'),
    path('divisionadd', views.division_form, name='division_add'),
    path('division/<int:divisionId>/', views.division_form, name='division_update'),
    path('division/delete/<int:divisionId>/', views.division_delete, name='division_delete'),
]
