from django.urls import path
from memo import views

app_name = 'memo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:stage_id>/update/', views.update, name='update'),
]
