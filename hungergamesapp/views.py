from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from .serializers import CustomersSerializer
from .models import Employees
from .serializers import EmployeeSerializer

class CustomersListCreateView(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

from .models import Employees
from .serializers import EmployeesSerializer

class EmployeesListCreateView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

from .models import Employee_salary_history
from .serializers import EmployeeSalaryHistorySerializer

class Employee_salary_historyListCreateView(generics.ListCreateAPIView):
    queryset = Employee_salary_history.objects.all()
    serializer_class = EmployeeSalaryHistorySerializer

from .models import MenuItems
from .serializers import MenuItemsSerializer

class MenuItemsListCreateView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

from .models import Orders
from .serializers import OrdersSerializer

class OrdersListCreateView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

from .models import Transactions
from .serializers import TransactionsSerializer

class TransactionsListCreateView(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

from .models import Deliveries
from .serializers import DeliveriesSerializer

class DeliveriesListCreateView(generics.ListCReateAPIView):
    queryset = Deliveries.objects.all()
    serializer_class = DeliveriesSerializer

class customerLoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        customer = authenticate(request, username=email, password=password)

        if customer is not None and customer.is_customer:
            login(request, customer)
            serializer = CustomersSerializer(customer)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class employeeLoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        employee = authenticate(request, username=email, password=password)

        if employee is not None and employee.is_employee:
            login(request, employee)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


