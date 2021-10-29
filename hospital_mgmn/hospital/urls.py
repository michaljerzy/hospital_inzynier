from django.urls import path
from hospital.views import About, Home, Contact, Login, Logout_admin,registerPage,loginPage

urlpatterns = [
    path('',Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    # path('admin_login/', Login, name = 'admin_login'),
    path('logout/', Logout_admin, name = 'logout_admin'),
    path("register/", registerPage, name = 'registerPage'),
    path("login/", loginPage, name = 'loginPage')
]
