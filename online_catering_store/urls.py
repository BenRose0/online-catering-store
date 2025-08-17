from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # customer site
    path('', include('catalog.urls')),

    # built-in auth views: gives you named URLs 'login' and 'logout'
    path('accounts/', include('django.contrib.auth.urls')),

    # your custom account routes (register, delete, etc.)
    path('accounts/', include('accounts.urls')),

    # if you added the cart
    # path('cart/', include('cart.urls')),
]
