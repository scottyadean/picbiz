import datetime
import json
from django.db import models
from taggit.managers import TaggableManager
from core.lib.date_helpers import fix_date, get_date_from_ts, format_date
from .directory import Directory
from .location import Location
from .company import Company
from .section import Section

class Manifest(models.Model):
    """
    Class to represent Manifest of dir. objects
    """
    name          = models.CharField("name", max_length=255)
    caption       = models.CharField("Caption", max_length=255, null=True, blank=True)
    subject       = models.CharField("Subject", max_length=255, default='', null=True, blank=True)

    directory     = models.ForeignKey(Directory, related_name='core_manifest_dir', on_delete=models.DO_NOTHING)
    location      = models.ForeignKey(Location, related_name='core_manifest_loc', on_delete=models.DO_NOTHING, default=1)
    section       = models.ForeignKey(Section, related_name='core_manifest_section', on_delete=models.DO_NOTHING, default=1)
    company       = models.ForeignKey(Company, related_name='core_manifest_company', on_delete=models.DO_NOTHING, default=1)
    sequence      = models.CharField("Sequence", max_length=255)

    thumb_path    = models.CharField("Thumb Path", max_length=500)
    src_path      = models.CharField("Src Path", max_length=500)

    import_status = models.CharField("Import Status", max_length=255, default='init' )

    date        = models.DateField("Date")
    exif_date   = models.DateTimeField("Date Time", null=True, blank=True)

    lat     = models.FloatField("lat", default=0)
    lng     = models.FloatField("lng", default=0)

    meta_1       = models.CharField("meta_1", max_length=255, default="", null=True, blank=True )
    meta_2       = models.CharField("meta_2", max_length=255, default="", null=True, blank=True )
    meta_3       = models.CharField("meta_3", max_length=255, default="", null=True, blank=True )

    tags         = TaggableManager()

    exif_data   = models.TextField("exif", null=True, blank=True)

    created_at  = models.DateTimeField("Created at", auto_now_add=True)
    updated_at  = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.name)

    def _format(req, row, status):
        data = {'name': row.get('name'),
                'subject': req.get('subject', ''),
                'caption': req.get('caption', ''),
                'directory_id': req.get('directory_id'),
                'company_id': req.get('company_id', 2),
                'location_id': req.get('location_id'),
                'section_id': req.get('section_id'),
                'src_path':"/static/{}/{}".format(req.get('dir'), row.get('name') ),
                'thumb_path': "/static/{}/thumbs/{}".format(req.get('dir'), row.get('name')),
                'sequence': req.get('seq',0),
                'import_status': status,
        }

        exif  = Manifest.get_exif(row['exif'].items(), ['DateTime', 'DateTimeOriginal', 'latlng'])
        try:
            data['exif_data'] = json.dumps(exif)
        except Excption as e:
            pass

        date  = Manifest.get_date(exif,  get_date_from_ts(row.get('file_date')) )
        data['date'] = format_date(date)
        data['exif_date'] = get_date_from_ts(row.get('file_date'))

        lat, lng = Manifest.get_lat_lng(exif.get('latlng', []))
        data['lat'] = lat
        data['lng'] = lng

        return data

    def get_exif(exif, extract=[]):
        meta = {}
        for k, v in exif:
            if k not in extract:
                continue
            if type(v) == bytes:
                v = v.decode("utf8", errors='ignore')
            meta[k] = str(v)
        return meta

    def get_lat_lng(lat_lng):
        if lat_lng and len(lat_lng) > 0:
            try:
                return [float(lat_lng[0]), float(lat_lng[1]) ]
            except Excption as e:
                pass
        return [0, 0]

    def get_date(exif, default_date):
        if 'DateTime' not in exif:
            return default_date
        d = default_date if exif['DateTime'] == None else exif['DateTime'];
        return d


    def default_fields():
        return ( 'id', 'name', 'caption', 'subject', 'directory_id', 'directory__name',
                 'date', 'exif_date', "import_status", 'company_id', 'company__name',
                 'lat', 'lng', 'location_id', 'location__name',  'section_id',
                 'section__name', 'sequence', 'src_path', 'thumb_path', 'created_at', 'updated_at'
                  )


    class Meta:
      pass
