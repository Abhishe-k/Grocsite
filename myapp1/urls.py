from django.urls import path
from . import views
app_name = 'myapp1'
urlpatterns = [
    path('', views.index, name='index'),
    path('myapp1/about/', views.about, name='about'),
    path('myapp1/<int:type_no>/', views.detail, name='detail')

]