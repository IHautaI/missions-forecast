from django.shortcuts import render, redirect

from forecast.models import Specialist, Award
from forecast.forms import RelevanceForm
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


def project(request, project_id):
    award = Award.objects.get(id=project_id)


    if request.method == 'POST':
        form = RelevanceForm(request.POST)
        if form.is_valid():

            award.relevant = form.save(commit=False).relevant
            award.save()

            return redirect('forecast:country', country_name=award.MBIO_name)

    else:
        form = RelevanceForm(instance=award)



    context = {'award': award, 'bool_form': form}
    return render(request, 'forecast/project.html', context)
