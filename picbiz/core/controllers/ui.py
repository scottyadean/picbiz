
from django.conf import settings
from core.lib.controller import Controller, login_required
from core.models.ui import UI


class UIController():
    actions = ['index', 'create', 'search', 'delete_all']

    def router(req, **kwargs):
        return Controller.route(UIController, UIController.actions, req, kwargs)

    def index(req):
        """ List the all UIs by type  """
        type = req.GET.get('type');
        uis = UI.objects.filter(**{'type':type}).order_by('name').values()
        return Controller.render_json({'results':list(uis), "total": len(uis)})

    def create(req):
        id = False
        if req.method == 'POST':
            nw = UI.objects.create(**{'name':req.POST.get('name'),
                                     'type':req.POST.get('type'),
                                     'markup':req.POST.get('markup'),
                                     'group':req.POST.get('group'),
                   })
            id = nw.id;
            nw.markup = nw.markup.format(nw.id)
            nw.save()
        return Controller.render_json({'success':True, 'id':id, })

    def search(req):
        """ List search results """
        f = {'name__icontains':req.GET.get('keyword', '')}
        locs = Section.objects.filter(**f).order_by('name').values('id', 'name')[:100]
        return Section.render_json({'sections':list(secs), "total": len(secs)})

    def delete_all(req):
        UI.objects.filter(**{}).delete()
        return Controller.render_json({'action':'delete_all'})
