from django.urls import path

from . import views

app_name = 'esearch'
urlpatterns = [
    path('', views.search_index, name='search_view'),
 #   path('<result>/', views.detail, name='detail'),
]
