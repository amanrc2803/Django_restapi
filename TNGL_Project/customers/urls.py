from django.urls import path
from .views import CustomerView

urlpatterns = [
    path('customers/', CustomerView.as_view(), name='customer-list'),
    path('customers/<int:pk>', CustomerView.as_view()),

    # Add other URL patterns as needed
]
