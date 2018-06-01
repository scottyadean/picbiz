import datetime
from django.conf import settings
from core.lib.controller import Controller, login_required

from core.models.directory import Directory
from core.models.location import Location
from core.models.section import Section
from core.models.manifest import Manifest


class ImageController():

  actions = ['index', 'search_sequance', 'get_sequence']

  def router(req, **kwargs):
    return Controller.route(ImageController, ImageController.actions, req, kwargs)

  def index(req):
    return Controller.goto('index/index.html')

  def search_sequance(req):
    f = {'date':req.GET.get('date', datetime.datetime.now()),
         'section_id': req.GET.get('section_id'),
         'company_id': req.GET.get('company_id'),
         'import_status': 'sequence'}
    sequences = Manifest.objects.filter(**f).distinct('sequence').values('sequence');
    return Controller.render_json({'results':list(sequences), "total": len(sequences)})

  def get_sequence(req):
      f = {'sequence': req.GET.get('sequence')}
      sequence = Manifest.objects.filter(**f).values(*Manifest.default_fields());
      return Controller.render_json({'results':list(sequence), "total": len(sequence)})
