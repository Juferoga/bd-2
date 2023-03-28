from django.urls import path, include

urlpatterns=[
    path('auth/', include('app.authentication.urls')),
    path('user/', include('app.user.urls')),
    # path('orders/', include('app.orders.urls')),
    # path('regions/', include('app.regions.urls')),
    # path('warehouse/', include('app.warehouse.urls')),
]