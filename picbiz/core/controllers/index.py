from core.lib.controller import Controller, login_required
from django.contrib.auth import authenticate, login, logout

class Index():
  
  def index(req):
    
    if req.user.is_authenticated:
      return Controller.goto('welcome')

    return Controller.render(req, {"errors":[]},  'login/login.html')
  
  def login(req):
      errors = []
      
      if req.user.is_authenticated:
        return Controller.goto('welcome')
      
      if req.method == "POST":
          username = req.POST.get('username')
          password = req.POST.get('password')
          user = authenticate(req, username=username, password=password)
          if user is not None:
             login(req, user)
             return Controller.goto('welcome')
          errors.append("Hmm I cant find that user/password combo")
          
      ctx = {"errors":errors}
      return Controller.render(req, ctx, 'login/login.html')
  
  @login_required
  def welcome(req):
    return Controller.render(req, {}, 'index/welcome.html')
  
  def logout(req):
    logout(req)
    return Controller.goto('index')