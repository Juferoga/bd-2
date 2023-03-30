from django.urls import path
from .views import AllProductsView, SaveProductView

urlpatterns = [
    path('python', AllProductsView.as_view(), name='all_products'),
    path('product/', SaveProductView.as_view(), name='save_product'),
]