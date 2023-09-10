"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path,include

from authentication import views
urlpatterns = [
   
    path('login/',views.login_page,name= 'login_page'),
    path('signup/',views.signup_page,name= 'signup_page'),
    path('logout/',views.logout_page,name= 'logout_page'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name= 'activate'),
    
]
