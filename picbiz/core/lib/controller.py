from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader

class Controller:
  
  def route(model, actions, req, kwargs, default='index'):
    """ Add to a controller to create action views on the fly """
    action = kwargs.get('action').replace('-', '_')
    if action not in actions:
      action = default
    return getattr(model, action)(req)
  
  def render(req, ctx, tpath):
      templ = loader.get_template(tpath)
      return HttpResponse(templ.render(ctx, req))

  def render_json(data, s=True):
    return JsonResponse(data, safe=s)

  def goto(url):
    return redirect(url)
  
  def update_attr(model, req, using='default'):
    
    name    = req.POST.get('name').strip()
    value   = req.POST.get('value').strip()
    pk      = int(req.POST.get('pk'))
    obj     = model.objects.using(using).get(pk=pk)
    
    setattr(obj, name, value)
    
    obj.save() 
    
    return {'success':True, 'pk':pk, 'name':name, 'value':value}
    