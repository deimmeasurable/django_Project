from django.contrib import admin

# Register your models here.
from natives.models import Native, Cohort

admin.site.register(Native)
admin.site.register(Cohort)