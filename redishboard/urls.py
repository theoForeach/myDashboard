from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'redishboard'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^api/data/$', views.get_data, name='api-data'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
    path('redishboard', views.IndexView.as_view(), name='index'),
    path('<str:key>/', views.detail, name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<str:key>/delete/', views.delete, name='delete'),
]
