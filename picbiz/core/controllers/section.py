from django.conf import settings
from core.lib.controller import Controller, login_required
from core.models.section import Section

class SectionController():
  actions = ['index', 'search']

  def router(req, **kwargs):
    return Controller.route(SectionController, SectionController.actions, req, kwargs)

  def index(req):
    """ List the all Sections  """
    secs = Section.objects.all().values()
    return Controller.render_json({'sections':list(secs), "total": len(secs)})

  def search(req):
    """ List search results """
    f = {'name__icontains':req.GET.get('keyword', '')}
    locs = Section.objects.filter(**f).order_by('name').values('id', 'name')[:100]
    return Section.render_json({'sections':list(secs), "total": len(secs)})
