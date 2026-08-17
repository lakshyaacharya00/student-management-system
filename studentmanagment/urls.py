"""
URL configuration for studentmanagment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from students import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path(
        'add_student/',
        views.add_student,
        name='add_student'
    ),

    path(
        'edit_student/<int:id>/',
        views.edit_student,
        name='edit_student'
    ),

    path(
        'delete_student/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),

    path(
        'student/<int:id>/',
        views.student_detail,
        name='student_detail'
    ),

path('login/', views.login_user, name='login'),

path('logout/', views.logout_user, name='logout'),
]