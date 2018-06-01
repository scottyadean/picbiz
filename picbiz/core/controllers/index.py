import datetime
from core.lib.controller import Controller, login_required
from django.contrib.auth import authenticate, login, logout
from core.models.company import Company
from core.models.section import Section

class Index():

  def index(req):
    company = Company.objects.all().exclude(name="Not Set").values('id', 'name')
    section = Section.objects.all().values('id', 'name')
    ctx = {"date": datetime.date.today().strftime("%Y-%m-%d"), "company":company, 'section':section}
    return Controller.render(req, ctx,'index/index.html')

  def login(req):
      errors = []
      if req.user.is_authenticated:
        return Controller.goto('/collect/index')

      if req.method == "POST":
          username = req.POST.get('username')
          password = req.POST.get('password')
          user = authenticate(req, username=username, password=password)
          if user is not None:
             login(req, user)
             return Controller.goto('/collect/index')
          errors.append("Hmm I cant find that user/password combo")

      ctx = {"errors":errors}
      return Controller.render(req, ctx, 'login/login.html')

  def logout(req):
    logout(req)
    return Controller.goto('index')
