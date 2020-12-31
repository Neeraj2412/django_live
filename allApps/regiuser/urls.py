
from django.urls import path, include
# from allApps.regiuser import urls
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('loginpg/', views.loginpg, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signuppg, name='signup'),
    path('sellerPortal/', views.sellerPage, name='sellerPortal'),
    # path('signup', views.signuppgUser, name='signup'),
]
