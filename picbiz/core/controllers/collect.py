import os
import json
import glob
import zipfile
from PIL import Image, ExifTags

from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from core.lib.controller import Controller, login_required
from core.lib.date_helpers import fix_date, get_date_from_ts, format_date
from core.lib.dict_helpers import index_by_dict
from core.lib.img_helpers import thumb_nail

from core.models.directory import Directory
from core.models.location import Location
from core.models.section import Section

class Collect():
  actions = ['index', 'import_img', 'save', 'upload', 'sort', 'thumbs']
  @login_required
  def router(req, **kwargs):
    return Controller.route(Collect, Collect.actions, req, kwargs)

  def index(req):
    """ List the dir. to process """
    current_dir = req.POST.get('current_dir', settings.UPLOAD_DIR)
    dirs = Collect.get_dir_list(current_dir)
    root = Collect.get_dir_list(settings.UPLOAD_ROOT, True)
    dir_list = []
    for d in dirs:
        path = "{}{}".format(current_dir, d)
        is_dir_in_db  = Directory.objects.filter(**{'full_path':path}).values('id', 'name', 'status')

        if len(is_dir_in_db) > 0 and is_dir_in_db[0]['status'] == 'done':
            continue

        status = is_dir_in_db[0]['status'] if len(is_dir_in_db) > 0 else "Not Processed"
        dir_list.append( {'name':d, 'status':status, 'path': path } )

    res = {'dir_list':dir_list, "total_dirs": len(dir_list), "root_path":settings.UPLOAD_ROOT, "root_dir":root, "current_dir":current_dir}
    return Controller.render(req, res, 'collect/index.html')

  def import_img(req):

    if req.method != 'POST':
        return Controller.goto('/collect/index')

    path  = req.POST.get('path')
    data  = {'status':'processing', 'name': os.path.basename(path), 'create_by': req.user.username }
    mkdir, created = Directory.objects.get_or_create(
      full_path=path,
      defaults=data,
    )

    sect  = req.POST.get('section-select')
    loc   = req.POST.get('location-select')
    # = Section.objects.get(id=1).values('id', 'name')
    sect_obj = Section.objects.filter(id=1).values('id', 'name')[0]
    loc_obj  = Location.objects.filter().values('id', 'name')[0]
    return Controller.render(req, {"path": path,
    "section_id":sect,
    'sect_obj':sect_obj,
    'loc_id':loc,
    'loc_obj':loc_obj,
    "mkdir": mkdir}, 'collect/import.html')


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

  def save(req):
    if req.method == "POST":
      return Controller.render_json({'params':req.POST})

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



  def get_dir_list(search_dir, reverse=False):
      """ Get dir list by path set reverse order for new created 1st """
      if not os.path.exists(search_dir):
          os.makedirs(search_dir)
      os.chdir(search_dir)
      dirs = list(filter(os.path.isdir, os.listdir(search_dir)))
      dirs.sort(key=lambda x: os.path.getmtime(x), reverse=reverse)
      return dirs
