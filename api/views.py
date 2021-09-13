from .models import Dataset
from rest_framework import viewsets
from .serializers import DatasetSerializer
from django.db.models import Q
from django.http import HttpResponse
import csv

class DatasetView(viewsets.ModelViewSet):
    serializer_class = DatasetSerializer

    def get_queryset(self):
        filter_name = self.kwargs.get('filter')
        return Dataset.objects.filter(
            Q(source__source__iexact=filter_name) | Q(country__iexact=filter_name)
        ).distinct() if filter_name else Dataset.objects.all()

def dataset_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="dataset.csv"'},
    )

    writer = csv.writer(response)
    for d in Dataset.objects.all():
        writer.writerow([
            f'Country - {d.country}',
            f'Category - {d.category}',
            'Brands - {}'.format(', '.join(map(str, d.brand.all()))),
            'Links - {}'.format(', '.join(map(str, d.link.all()))),
            'Sources - {}'.format(', '.join(map(str, d.source.all()))),
        ])

    return response
