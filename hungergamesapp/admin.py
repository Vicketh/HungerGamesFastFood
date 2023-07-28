from django.contrib import admin
from .models import Employees, Employee_salary_history, Customers, MenuItems, Orders, Transactions, Deliveries

# Registered models.

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_first_name', 'employee_last_name')
    search_fields = ('employee_first_name', 'employee_last_name')
    list_per_page = 20

@admin.register(Employee_salary_history)
class EmployeeSalaryHistoryAdmin(admin.ModelAdmin):
    list_display = ('salary_id', 'employee_id', 'salary_amount', 'effective_date')
    list_filter = ('effective_date',)
    search_fields = ('employee_id__employee_first_name', 'employee_id__employee_last_name')
    list_per_page = 20

    def salary_amount(self, obj):
        return obj.salary.get('amount')

    salary_amount.short_description = 'Salary Amount'

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('Customer_id', 'customer_first_name', 'customer_last_name', 'customer_phonenumber')
    list_filter = ('customer_phonenumber',)
    search_fields = ('customer_id__customer_first_name', 'customer_id__customer__lastname')
    list_per_page = 20

@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ('MenuItem_id', 'MenuItem_name', 'MenuItem_Description')
    search_fields = ('MenuItem_id__MenuItem_name', 'MenuItem_id__MenuItem_description')
    list_per_page = 30

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('Order_id', 'Order_details', 'customer_id')
    list_filter = ()
    search_fields = ('customer_id__order_details', 'order_id__order_details', 'order_id__customer_id')
    list_per_page = 30

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('Transaction_id', 'customer_id', 'order_id', 'transaction_date', 'payment_info')
    list_filter = ('transaction_date', 'payment_info')
    search_fields = ('transaction_id__customer_id', 'transaction_id__order_id', 'customer_id__order_id', 'customer_id__payment_info', 'transaction_id__payment_info')
    list_per_page = 50

@admin.register(Deliveries)
class DeliveriesAdmin(admin.ModelAdmin):
    list_display = ('Delivery_id', 'customer_id', 'order_id', 'Delivery_status', 'Delivery_items')
    list_filter = ('Delivery_status', 'Delivery_items')
    search_fields = ('customer_id__order_id', 'delivery_id__order_id', 'customer_id__Delivery_items', 'delivery_id__Delivery_items', 'delivery_id__delivery_status', 'Delivery_items__Delivery_status')
    list_per_page = 50