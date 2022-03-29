from django.urls import path
from . import views
app_name = 'myapp1'
urlpatterns = [
    path('', views.index, name='index'),
    path('myapp1/about/', views.about, name='about'),
    path('myapp1/<int:type_no>/', views.detail, name='detail'),
    path('myapp1/items', views.items, name='item'),
    path('myapp1/placeorder', views.placeorder, name='placeorder'),

]