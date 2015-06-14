from django.shortcuts import render

from forecast.models import Specialist, Award
# Create your views here.
def specialist(request, specialist_id):
    specialist = Specialist.objects.get(id=specialist_id)
    context = {'specialist':specialist, \
               'projects':specialist.award_set.all()}
    return render(request, 'forecast/specialist.html', context)

def country(request, country_name):
    awards = Award.objects.filter(MBIO_name=country_name)
    context = {'country':country_name, 'projects':awards}
    return render(request, 'forecast/country.html', context)

def NAICS(request, code):
    awards = Award.objects.filter(details__NAICS_code=code)
    context = {'NAICS_code':code, 'projects':awards}
    return render(request, 'forecast/NAICS.html', context)
