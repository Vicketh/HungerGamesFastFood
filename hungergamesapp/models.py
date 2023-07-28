from django.db import models

# In models.py of the hungergamesapp

from django.db import models

class Customers(models.Model):
    # customers table
    customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50)
    customer_nickname = models.CharField(max_length=20)

class Employees(models.Model):
    # employees table
    employee_id = models.AutoField(primary_key=True)
    employee_first_name = models.CharField(max_length=50)
    employee_last_name = models.CharField(max_length=50)

class Employee_salary_history(models.Model):
    #Employee salary History table
    salary_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    salary_history = models.JSONField()
    effective_date = models.DateField()
    
class MenuItems(models.Model):
    # MenuItems table
    MenuItem_id = models.AutoField(primary_key=True)
    MenuItem_name = models.CharField(max_length=50)
    MenuItem_description = models.JSONField()

class Orders(models.Model):
    # Orders table
    Order_id = models.AutoField(primary_key=True)
    Order_details = models.JSONField()
    Customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)

class Transactions(models.Model):
    # Transactions table
    Transaction_id = models.AutoField(primary_key=True)
    Customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Transaction_date = models.DateField()
    payment_info = models.JSONField()

class Deliveries(models.Model):
    #Deliveries table
    Delivery_id = models.AutoField(primary_key=True)
    Customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    Order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Delivery_items = models.JSONField()
    Delivery_status = models.CharField(max_length=50)