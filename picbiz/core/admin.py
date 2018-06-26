
from django.contrib import admin
from core.models.directory import Directory
from core.models.location import Location
from core.models.manifest import Manifest
from core.models.company import Company
from core.models.section import Section
from core.models.custdata import Custdata
admin.site.site_header = 'Data Administration'

admin.site.register(Directory)
admin.site.register(Location)
admin.site.register(Manifest)
admin.site.register(Company)
admin.site.register(Section)
admin.site.register(Custdata)
