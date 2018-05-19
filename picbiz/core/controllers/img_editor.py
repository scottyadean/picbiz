import os
from PIL import Image
import glob
import zipfile
from django.conf import settings
from core.lib.controller import Controller, login_required
from core.lib.img_helpers import thumb_nail
from django.contrib.auth import authenticate, login, logout


class ImgEditor():
  
  actions = ['index', 'rotate']
  
  @login_required
  def router(req, **kwargs):
    return Controller.route(ImgEditor, ImgEditor.actions, req, kwargs)
  
  def index(req):
    return Controller.render(req, {}, 'collect/index.html')
  
  def rotate(req):
    _dir  = req.GET.get('dir')
    _file = req.GET.get('file_name')
    _path = "{}{}/{}".format(settings.UPLOAD_DIR, _dir, _file)
    _thumb ="{}{}/thumbs/".format(settings.UPLOAD_DIR, _dir)
    img = Image.open(_path)
    img = img.rotate(90)
    img.save(_path)
    thumb_nail([_path], _thumb, (500, 500))
    
    return Controller.render_json({'dir':_dir, 'file_name':_file, 'path':_path})