from django.contrib import admin
from django.urls import path
from .views import CustomersListCreateView, EmployeesListCreateView, MenuItemsListCreateView, DeliveriesListCreateView
from .views import OrdersListCreateView, TransactionsListCreateView, CustomerLoginView, EmployeeLoginView

urlpatterns = [
    path('customers/', CustomersListCreateView.as_view(), name='customers-list-create'),
    path('employees/', EmployeesListCreateView.as_view(), name='employees-list-create'),
    path('menuitems/', MenuItemsListCreateView.as_view(), name='menuitems-list-create'),
    path('orders/', OrdersListCreateView.as_view(), name='orders-list-create'),
    path('transactions/', TransactionsListCreateView.as_view(), name='transactions-list-create'),
    path('deliveries/', DeliveriesListCreateView.as_view(), name='deliveries-list-create'),
    path('login/customer/', CustomerLoginView.as_view(), name='customer-login'),
    path('login/employee/', EmployeeLoginView.as_view(), name='employee-login'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
]
