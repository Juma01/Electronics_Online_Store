from django.contrib import admin
from django.urls import path
from products.views import main_view, phones_view, phone_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', phones_view),
    path('products/<int:phone_id>/', phone_detail_view)
]
