import os
import json
import glob
import zipfile
from PIL import Image, ExifTags

from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from core.lib.controller import Controller, login_required
from core.lib.date_helpers import fix_date, get_date_from_ts, format_date
from core.lib.dict_helpers import index_by_dict
from core.lib.img_helpers import thumb_nail

from core.models.directory import Directory
from core.models.location import Location

class Collect():

  actions = ['index', 'import_img', 'upload', 'sort', 'thumbs']

  @login_required
  def router(req, **kwargs):
    return Controller.route(Collect, Collect.actions, req, kwargs)

  def index(req):
    """ List the dir. to process """
    search_dir = settings.UPLOAD_DIR
    os.chdir(search_dir)
    dirs = list(filter(os.path.isdir, os.listdir(search_dir)))
    dirs.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    dir_in_db   = Directory.objects.filter(**{}).exclude(status='done').values('id', 'name', 'status')
    indexed_dir = index_by_dict(dir_in_db, 'name')
    dir_list = []
    for d in dirs:
      db_info = indexed_dir.get(d, None)
      status = "Not Processed" if db_info == None else "Pending Import"
      dir_list.append( {'name':d, 'db_info':db_info, 'status':status, 'path': "{}{}".format(settings.UPLOAD_DIR, d) } )

    return Controller.render(req, {'dir_list':dir_list, "total_dirs": len(dir_list)}, 'collect/index.html')

  def import_img(req):
    path  = req.POST.get('path')
    data  = {'status':'processing', 'name': os.path.basename(path), 'create_by': req.user.username }
    mkdir, created = Directory.objects.get_or_create(
      full_path=path,
      defaults=data,
    )
    return Controller.render(req, {"path": path, "mkdir": mkdir}, 'collect/import.html')


  def upload(req):
    if req.method == 'POST':
      fname = "{}{}".format(settings.UPLOAD_DIR, req.POST.get('name'))
      with zipfile.ZipFile(req.FILES['images'],"r") as zip_ref:
        zip_ref.extractall(fname)
      return Collect.sort(req, name=fname)

    else:
      return Controller.render(req, {}, 'collect/form.html')

  def sort(req, **kwargs):
    return Controller.render(req, {'path': kwargs.get('name')}, 'collect/sort.html')


  def thumbs(req):
    _dir = req.POST.get('dir')
    img_dir = "{}{}/*.jpg".format(settings.UPLOAD_DIR, _dir)
    out_dir = "{}{}/thumbs/".format(settings.UPLOAD_DIR, _dir)
    meta_data = thumb_nail(glob.glob(img_dir), out_dir, (500, 500))
    meta_dict = {}

    for key, val in meta_data.items():
      temp_dict = {}
      temp_dict['latlng'] = val['latlng']
      temp_dict['name']   = val['name']
      temp_dict['path']   = val['path']
      temp_dict['src']    = "/static/{}/{}".format(_dir, val['name'])
      temp_dict['thumb']  = "/static/{}/thumbs/{}".format(_dir, val['name'])
      temp_dict['dir']    =  _dir
      temp_dict['file_date'] = get_date_from_ts(val['file_date'])
      temp_dict['exif_date'] = None;
      for k, v in val['exif'].items():
        if type(v) == bytes:
          v = v.decode("utf8", errors='ignore')
        temp_dict[k] = str(v)
        if k == 'DateTime':
          temp_dict['exif_date'] = format_date(str(v))


      meta_dict[key] = temp_dict

    return Controller.render_json({'meta_data': meta_dict}, True)






  # def update_attr(req):
  #   return Controller.render_json(Controller.update_attr(Client, req, 'obi'))
