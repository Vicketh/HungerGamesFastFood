from django.test import TestCase
from .models import Employees, Employee_salary_history, Customers
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class EmployeesModelTestCase(TestCase):
    def setUp(self):
        Employees.objects.create(employee_first_name='John', employee_last_name='Doe')
        Employees.objects.create(employee_first_name='Jane', employee_last_name='Smith')

    def test_employee_names(self):
        john = Employees.objects.get(employee_first_name='John')
        jane = Employees.objects.get(employee_first_name='Jane')
        self.assertEqual(john.employee_last_name, 'Doe')
        self.assertEqual(jane.employee_last_name, 'Smith')

class EmployeeSalaryHistoryModelTestCase(TestCase):
    def setUp(self):
        employee = Employees.objects.create(employee_first_name='John', employee_last_name='Doe')
        Employee_salary_history.objects.create(employee=employee, employee_salary=50000)
        Employee_salary_history.objects.create(employee=employee, employee_salary=55000)

    def test_employee_salary(self):
        john = Employees.objects.get(employee_first_name='John')
        salary_history = Employee_salary_history.objects.filter(employee=john)
        self.assertEqual(salary_history.count(), 2)

class EmployeesAPITestCase(APITestCase):
    def setUp(self):
        Employees.objects.create(employee_first_name='John', employee_last_name='Doe')
        Employees.objects.create(employee_first_name='Jane', employee_last_name='Smith')

    def test_get_employees_list(self):
        url = reverse('employees-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_employee(self):
        url = reverse('employees-list')
        data = {'employee_first_name': 'Alice', 'employee_last_name': 'Johnson'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employees.objects.count(), 3)

    def test_update_employee(self):
        john = Employees.objects.get(employee_first_name='John')
        url = reverse('employees-detail', args=[john.pk])
        data = {'employee_first_name': 'Johnny', 'employee_last_name': 'Doe'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        john.refresh_from_db()
        self.assertEqual(john.employee_first_name, 'Johnny')

    def test_delete_employee(self):
        jane = Employees.objects.get(employee_first_name='Jane')
        url = reverse('employees-detail', args=[jane.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employees.objects.count(), 1)

class CustomersAPITestCase(APITestCase):
    def setUp(self):
        Customers.objects.create(Customer_FirstName='John', Customer_LastName='Doe')
        Customers.objects.create(Customer_FirstName='Jane', Customer_LastName='Smith')

    def test_get_customers_list(self):
        url = reverse('customers-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_customer(self):
        url = reverse('customers-list')
        data = {'Customer_FirstName': 'Alice', 'Customer_LastName': 'Johnson'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customers.objects.count(), 3)

    def test_update_customer(self):
        john = Customers.objects.get(Customer_FirstName='John')
        url = reverse('customers-detail', args=[john.pk])
        data = {'Customer_FirstName': 'Johnny', 'Customer_LastName': 'Doe'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        john.refresh_from_db()
        self.assertEqual(john.Customer_FirstName, 'Johnny')

    def test_delete_customer(self):
        jane = Customers.objects.get(Customer_FirstName='Jane')
        url = reverse('customers-detail', args=[jane.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customers.objects.count(), 1)