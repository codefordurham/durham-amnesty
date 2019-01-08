from django.contrib import admin

from .models import Applicant, CourtRecord

admin.site.register(Applicant)
admin.site.register(CourtRecord)