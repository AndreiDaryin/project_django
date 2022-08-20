from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('add-to-cart', views.AddToCart.as_view(), name="add-to-cart"),
    path('delete-from-cart/<int:pk>', views.DeleteFromCart.as_view(), name="delete-from-cart"),
    path('update-cart/<int:pk>', views.UpdateCart.as_view(), name="update-cart"),
    path('order-list', views.OrderList.as_view(), name="order-list"),
    path('order-view/<int:pk>', views.OrderView.as_view(), name="order-view"),
    path('order-edit/<int:pk>', views.OrderEditView.as_view(), name="order-edit"),
]