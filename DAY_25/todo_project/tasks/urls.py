from django.urls import path
from tasks.views import *


urlpatterns = [
    path('',Register_page,name='register-page'),
    path('login/',login_page,name='login-page'),
    path('logout/',logout_page,name='logout_page'),
    path('home-page/',home_page,name='home_page'),
    path('profile/',profile_page,name = 'profile_page' ),
    path('update_profile/', profile_update,name = 'profile_update'),
    path('product-list/',product_list,name='product_list')
]
