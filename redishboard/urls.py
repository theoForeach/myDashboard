from django.urls import path
from . import views

app_name = 'redishboard'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<str:key>/delete/', views.delete, name='delete'),
]
