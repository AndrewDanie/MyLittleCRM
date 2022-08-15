from django.urls import path
from . import views

urlpatterns = [
    path('orderlist', views.OrderAPIList.as_view()),
    path('add_order', views.add_order)
]