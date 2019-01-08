from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .forms import StatusForm
from .models import Applicant, CourtRecord

def index(request):
	if request.method == 'POST':
		form = StatusForm(request.POST)
		if form.is_valid():
			driver_license_number=form.cleaned_data['driver_license_number']
			return HttpResponseRedirect('/status/'+driver_license_number+'/records')
	else:
		form = StatusForm()
	return render(request, 'status/index.html', {'form':form})
	
def records(request,driver_license_number):
	records= CourtRecord.objects.filter(driver_license_number=driver_license_number)
	template = loader.get_template('status/records.html')
	context = {'records':records,}
	return HttpResponse(template.render(context,request))