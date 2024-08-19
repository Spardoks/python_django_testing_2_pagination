import csv

from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV

CONTENT = []
with open(BUS_STATION_CSV, encoding='UTF-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        CONTENT.append(
            {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
        )


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))

    paginator = Paginator(CONTENT, 10)
    stations = paginator.get_page(page_number)

    context = {
        'bus_stations': stations,
        'page': stations,
    }
    return render(request, 'stations/index.html', context)
