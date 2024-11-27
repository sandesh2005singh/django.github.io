from django.contrib import admin
from django.urls import path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="Home"),
    path('contact',views.contact, name="Contact"),
    path('login',views.login, name="Login"),


]
