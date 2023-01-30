from django.contrib import admin
from django.urls import path
from products.views import main_view, phones_view, phone_detail_view, create_product_view
from Electronics_Online_Store.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from users.views import auth_view, logout_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', phones_view),
    path('products/<int:phone_id>/', phone_detail_view),
    path('products/create/', create_product_view),

    # users
    path('users/login/', auth_view),
    path('users/logout/', logout_view),
    path('users/register/', register_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
