//red, green, blue, egg yolk yellow, orange, purple, brown, black
  const  img_edit = {
    rotation_count:0,

    rotation:function(el){
      console.log(el);
      let dr = el.getAttribute("data-dir");
      let fn = el.getAttribute("data-src");
      img_edit.rotation_count += 1;
     _app.xhr_get('/img/edit/rotate', {'dir':dr, 'file_name': fn}, function(e){

      img = _app.el('img-'+fn);
      img_src = img.getAttribute('data-src');
      img.src = img_src += '?ver='+img_edit.rotation_count;
      console.log(_app.xhr_res(e));  } );
    },

    get_locations:function(){
      _scan.msg.innerHTML = 'Downloading Locations';
      _app.xhr_get('/location/index', {}, function(e){
      _scan.locs = _app.xhr_res(e).locations;
    });
    },
    get_meta:function(img){
      _scan.msg.innerHTML = 'Perdicting Meta Data';
      _scan.imgs = img;
      _.forOwn(img, function(v, k) {
            d = (v.exif_date === null) ? v.file_date : v.exif_date;
            dt = v.hasOwnProperty('DateTimeOriginal') ? ( v.DateTimeOriginal || d) : d;
            _app.el('img-'+v.name+'-date').value = d;
            _app.el('img-'+v.name+'-datetime').value = dt;
      });
    },

   get_latlng_value:(v)=> {
     if(v.latlng !== null && v.latlng.length > 1 && v.latlng[0] !== null) {
      return {lat:v.latlng[0], lng:v.latlng[1]};
     }else{
      return {lat:0, lng:0};
     }
   },

    get_latlng:(v)=>{
      if(v.latlng !== null && v.latlng[0] !== null){
         _scan.msg.innerHTML = 'Location for'+k;
         loc = _scan.get_geo(v.latlng);
         if (loc !== null){
          _app.el('img-'+v.name+'-loc-display').innerHTML = loc.name;
          _app.el('img-'+v.name+'-loc').value = loc.id;
          _app.el('img-'+v.name+'-section-display').innerHTML = loc.section__name;
          _app.el('img-'+v.name+'-section').value = loc.section_id;
         }
      }
    },


    get_geo:function(latlng){
        var loc = null;
        var diff = 0;
        for(var key in _scan.locs){
          v = _scan.locs[key];
          if(loc === null) {
           diff = _scan.distance(v.lat, v.lng, latlng[0], latlng[1]);
           if (diff < 1.1){loc = v; break;}
          }
        }
      return loc;
    },


  distance:function(lat1, lon1, lat2, lon2) {
  // Converts numeric degrees to radians
  var toRad = function(Value) { return Value * Math.PI / 180;};
    var R = 6371; // km
    var dLat = toRad(lat2-lat1);
    var dLon = toRad(lon2-lon1);
    lat1 = toRad(lat1);
    lat2 = toRad(lat2);
    var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
      Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    var d = R * c;
    return d;
  },




};
