from django.urls import path
from . import views

urlpatterns = [
	path('', views.api_overview, name="api_overview"),
	path('get_all_employees/', views.get_all_employees, name="get_all_employees"),
	path('get_employee_by_id/<str:pk>/', views.get_employee_by_id, name="get_employee_by_id"),
	path('generate_fake_data/<int:number>/', views.generate_fake_data, name="generate_fake_data"),
	path('create_new_employee/', views.create_new_employee, name="create_new_employee"),
]
