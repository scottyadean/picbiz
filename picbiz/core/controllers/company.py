from django.conf import settings
from core.lib.controller import Controller, login_required
from core.models.company import Company

class CompanyController():

  actions = ['index', 'search']

  def router(req, **kwargs):
    return Controller.route(CompanyController, CompanyController.actions, req, kwargs)

  def index(req):
    """ List the all companies  """
    companies = Company.objects.all().values()
    return Controller.render_json({'companies':list(companies), "total_companies": len(companies)})

  def search(req):
    """ List search results """
    f = {'name__icontains':req.GET.get('keyword', '')}
    companies = Company.objects.filter(**f).order_by('name').values('id', 'name')[:100]
    return Controller.render_json({'companies':list(companies), "total_companies": len(companies)})
