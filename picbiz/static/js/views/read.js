
  const _scan = {

      init:function(params){
       this.path = params.path;
       this.sect_id = params.section_id;
       this.sect_name = params.ection_name;
       this.loc_id = params.location_id;
       this.loc_name = params.location_name;
       this.dir = params.directory_name;
       this.dir_id = params.directory_id;
       this.msg = _app.el('import-message');
       this.events();
       this.list();
      },

      events:()=>{
       _app.event_add(_app.el('save_seq'), 'click', _scan.save );
       _app.event_bind('file-list', 'click', _scan.delegate);
      },

     save:(e)=>{
       var checkboxes = _app.query_dom("input[type='checkbox']:checked");
       var sequence = [];
       var res;
       checkboxes.forEach( (node, idx)=>{ sequence.push( node.value )  })
       checkboxes.forEach( (node, idx)=>{
         form = _app.el('form-'+node.value);
         params = _app.xhr_form_data(form.getElementsByTagName('input'));
         params['sequence'] = sequence.join("|");
         params['dom_id'] = 'form-'+node.value;
         _app.xhr_post('/collect/update', params, (e)=>{
             res = _app.xhr_res(e).params;
            _app.el(res.dom_id).remove();
         });
       });
     },

     delegate:(e)=>{
         if (e.target && e.target.matches("a.rotate")){ img_edit.rotation(e.target);}
         if (e.target && e.target.matches("img.modal")){ _scan.modal(e.target);  }
      },

      list:()=>{
       var params = {path: _scan.path,
                     dir: _scan.dir,
                     directory_id:_scan.dir_id,
                     section_id:_scan.sect_id,
                     location_id:_scan.loc_id,
                    }
     _scan.msg.innerHTML = 'Buiding Thumbnails';
        _app.xhr_post('/collect/create', params,  _scan.list_load);
     },

     list_load:function(e){
       let img   = _app.xhr_res(e).success;
       _scan.msg.innerHTML = 'Buiding List';
       _app.xhr_get('/collect/manifest', {directory_id:_scan.dir_id}, (e)=>{

          var img = _app.xhr_res(e).results;
          let tmp   = _.template(_app.el('file-list-temp').innerHTML);
          let ele   = _app.el('file-list');
          let total = img.length-1;
          _scan.msg.innerHTML = 'Adding images';
          _.forOwn(img, function(v, k) {
              _scan.msg.innerHTML = 'Adding image: '+v.name;
             _app.el_html(ele, tmp({idx:k, val:v, dir:_scan.dir, total:total}));
            });
             _scan.msg.innerHTML = 'Scan Complete:'
       });

     }, //get list load

    modal:function(e) {
     var src = e.getAttribute('data-src');
      // initialize modal element
      var mod = document.createElement('div');
      var img = document.createElement('img');
      var div = document.createElement('div');

      img.src = src;
      img = _app.css.style(img, {width:'auto', height:'auto', display: 'block', maxWidth:'750px',
                                 margin:'2px',maxHeight:'550px', maxHeight:'850px'
                           });

      mod = _app.css.style(mod, {
       width:'75%',height:'75%',margin:'100px auto',
       overflow:'hidden',backgroundColor:'#fff',overflowY:'auto',height:'300px',
      });

      mod.appendChild(img);
      div.innerHTML = "exif"
      mod.appendChild( div );
      mui.overlay('on', mod);
  }

};
