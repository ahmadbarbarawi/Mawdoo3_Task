from . import create_fake_data
from .models import Employees
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from .serializers import EmployeeSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls={
        'List all employees':"/get_all_employees/",
        'List Employee by ID':"/get_employee_by_id/",
        'Create New Employee':"/create_new_employee/",
        'create_fake_data':"/generate_fake_data/",
    }
    return Response(api_urls)
@api_view(['GET'])
def get_all_employees(request):
    employees=Employees.objects.all()
    if employees .exists():
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    else:
        return Response(status=200,data='The table is empty')



@api_view(['GET'])
def get_employee_by_id(request,pk):
    try:
        employee=Employees.objects.get(id=pk)
        serializer=EmployeeSerializer(employee,many=False)
        return Response(serializer.data)
    except:
        return Response(status=HTTP_404_NOT_FOUND,data='No employee with id: '+pk)


@api_view(['POST'])
def create_new_employee(request):
    serializer=EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=201,data='The data format is not valid')

@api_view(['GET'])
def generate_fake_data(request,number):
    gfd=create_fake_data.fake_data(number)
    gfd.create_employees()

    return Response(status=201,data='The fake data added successfully')
