from django.urls import path

from core.controllers.index import Index
from core.controllers.collect import Collect
from core.controllers.img_editor import ImgEditor
from core.controllers.company import CompanyController
from core.controllers.location import LocationController
from core.controllers.section import SectionController

urlpatterns = [
    path(r'', Index.index, name='index'),
    path(r'login', Index.login, name='login'),
    path(r'logout', Index.logout, name='logout'),
    path(r'welcome', Index.welcome, name='welcome'),

    path(r'collect/<str:action>', Collect.router, name='core-collect-router'),
    path(r'img/edit/<str:action>', ImgEditor.router, name='core-img-edit-router'),
    path(r'company/<str:action>', CompanyController.router, name='core-company-router'),
    path(r'location/<str:action>', LocationController.router, name='core-location-router'),
    path(r'section/<str:action>', SectionController.router, name='core-section-router'),

]
