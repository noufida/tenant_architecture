
from django.urls import path
from . import views 

urlpatterns = [
    path('products/',views.my_products, name='get_products'),

]
