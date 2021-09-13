from django.urls import path
from .views import DatasetView, dataset_csv

urlpatterns = [
    path('dataset/', DatasetView.as_view({'get' : 'list', 'post' : 'create'}), name='dataset'),
    path('dataset/<str:filter>', DatasetView.as_view({'get' : 'list'}), name='dataset'),
    path('dataset_csv', dataset_csv, name='dataset_csv'),
] 