"""
URL configuration for i_wish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from i_wish import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("add_wish/",views.add_zelanie,name="add_wish"),

    path("delete_wish/<int:zel_id>",views.confirm_delete, name="delete_wish"),
    path("wish_list/<int:pol_id>",views.wish_list,name="wish_list"),
    path("accounts/login/",LoginView.as_view(next_page="wish_list"),name="login"),
    path("accounts/logout/",LogoutView.as_view(next_page="login"),name="logout"),
    path("registration/", views.registration, name="registration")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)