from django.contrib import admin

from .models import (Customers, Deliveries, Employee_salary_history, Employees,
                     MenuItems, Orders, Transactions)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_first_name', 'employee_last_name')
    search_fields = ('employee_first_name', 'employee_last_name')
    list_per_page = 20


@admin.register(Employee_salary_history)
class EmployeeSalaryHistoryAdmin(admin.ModelAdmin):
    list_display = ('salary_id', 'employee_id',
                    'salary_amount', 'effective_date')
    list_filter = ('effective_date',)
    search_fields = ('employee_id__employee_first_name',
                     'employee_id__employee_last_name')
    list_per_page = 20

    def salary_amount(self, obj):
        return obj.salary.get('amount')

    salary_amount.short_description = 'Salary Amount'


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('Customer_id', 'customer_first_name',
                    'customer_last_name', 'customer_phonenumber')
    list_filter = ('customer_phonenumber',)
    list_per_page = 20


@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('MenuItem_id', 'MenuItem_name', 'MenuItem_description')
    search_fields = ('MenuItem_id__MenuItem_name',
                     'MenuItem_id__MenuItem_description')
    list_per_page = 30


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('Order_id', 'Order_details', 'Customer_id')
    list_filter = ()
    search_fields = ('Customer_id__Order_details',
                     'Order_id__Order_details', 'Order_id__Customer_id')
    list_per_page = 30


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('Transaction_id', 'Customer_id', 'Order_id',
                    'Transaction_date', 'payment_info')
    # Use lowercase field names
    list_filter = ('Transaction_date', 'payment_info')
    search_fields = ('Transaction_id__Customer_id', 'Transaction_id__Order_id',  # Use lowercase field names
                     'Customer_id__Order_id', 'Customer_id__payment_info', 'Transaction_id__payment_info')
    list_per_page = 50


@admin.register(Deliveries)
class DeliveriesAdmin(admin.ModelAdmin):
    list_display = ('Delivery_id', 'customer_id', 'order_id',
                    'Delivery_status', 'Delivery_items')
    list_filter = ('Delivery_status', 'Delivery_items')
    list_per_page = 50
