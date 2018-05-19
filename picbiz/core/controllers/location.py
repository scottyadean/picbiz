from django.conf import settings
from core.lib.controller import Controller, login_required
from core.models.location import Location

class LocationController():
  actions = ['index', 'search']

  def router(req, **kwargs):
    return Controller.route(LocationController, LocationController.actions, req, kwargs)

  def index(req):
    """ List the all locations  """
    v = ('id', 'name', 'section_id', 'section__name', 'lat', 'lng')
    locs = Location.objects.filter(**{}).values(*v)
    return Controller.render_json({'locations':list(locs), "total": len(locs)})

  def search(req):
    """ List search results """
    f = {'name__icontains':req.GET.get('keyword', '')}
    locs = Location.objects.filter(**f).order_by('name').values('id', 'name')[:100]
    return Location.render_json({'locations':list(locs), "total": len(locs)})
