from django.urls import path
from pagination_app import views

app_name = 'pagination_app'


urlpatterns = [
    path('', views.booklist, name='index'),
]
