from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('stocks/', include('StocksApp.urls')),
    path('admin/', admin.site.urls),
]
