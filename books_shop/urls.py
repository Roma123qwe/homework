import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/", include("sales_manager.urls")),
    path('hotel/', include('hotel_room.urls')),
    path('account/', include('sales_manager.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('lokal_hotel/', include('lokal_hotel.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
