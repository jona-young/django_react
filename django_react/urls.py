"""django_react URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts import views as accounts_views
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', IndexView.as_view()),
    # from the users application, and 'register' is the name of the function within the views.py
    path('register/', accounts_views.register, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    # 'login/' is the name of the url in the browser, 'auth_views' is the views.py imported from
    # 'django.contrib.auth', and 'LoginView.as_view()' is a class of that views.py
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # 'as_view(templatename='users/login.html')' redirects Django to look in that directory instead
    # of the default 'register/login.html'
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view
    (template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view
    (template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view
    (template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view
    (template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]
