
from django.contrib import admin
from core.models.directory import Directory
from core.models.location import Location
from core.models.mainfest import Mainfest
from core.models.company import Company
from core.models.section import Section

admin.site.site_header = 'Data Administration'

admin.site.register(Directory)
admin.site.register(Location)
admin.site.register(Mainfest)
admin.site.register(Company)
admin.site.register(Section)
