from django.contrib import admin
from django.urls import path, include
from .views import Create_Transaction , Get_Transactions

urlpatterns = [
    path('payment/', Create_Transaction.as_view(), name="create_tranaction"),
    path('payment/get/', Get_Transactions.as_view(), name="get_transaction")
]
