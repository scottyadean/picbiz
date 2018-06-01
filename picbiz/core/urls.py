from django.urls import path

from core.controllers.index import Index
from core.controllers.collect import Collect
from core.controllers.img_editor import ImgEditor
from core.controllers.images import ImageController
from core.controllers.company import CompanyController
from core.controllers.location import LocationController
from core.controllers.section import SectionController
from core.controllers.ui import UIController

urlpatterns = [
    path(r'', Index.index, name='index'),
    path(r'login', Index.login, name='login'),
    path(r'accounts/login/', Index.login, name='login-next'),
    path(r'logout', Index.logout, name='logout'),

    path(r'collect/<str:action>', Collect.router, name='core-collect-router'),
    path(r'img/edit/<str:action>', ImgEditor.router, name='core-img-edit-router'),

    path(r'images/<str:action>', ImageController.router, name='core-img-router'),

    path(r'company/<str:action>', CompanyController.router, name='core-company-router'),
    path(r'location/<str:action>', LocationController.router, name='core-location-router'),
    path(r'section/<str:action>', SectionController.router, name='core-section-router'),
    path(r'ui/<str:action>', UIController.router, name='core-ui-router'),

]
