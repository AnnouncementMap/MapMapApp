from django.contrib import admin
from django.urls import path
from datamap import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_response/', views.test_response),
]
