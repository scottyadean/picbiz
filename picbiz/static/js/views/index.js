
const _images = {
     img_results:[],
     cycle_index:[],
     time_out:false,

     init:(e)=>{
      $(".select2").select2({tags: false, selectOnBlur: true, multiple: false});
      _app.event_add(_app.el('trigger-search'), 'click', (e)=>{ _images.search(this.target);});
       $('#display-sequence').delegate('img.sm-img', 'mouseover', _images.delegate);
       $('#display-sequence').delegate('img.sm-img', 'click', _images.slides.build);
       $('#display-sequence').delegate('img.sm-img', 'mouseout', (e)=>{
        (_images.time_out) ? clearTimeout(_images.time_out) : false;
        _images.cycle_run = false;
        _images.time_out = false
       });
     },

     delegate:(e)=>{
         var el = e.target;
         if (el && el.matches("img.sm-img")){
             _images.cycle_index  = 1;
             _images.cycle_run    = true;
             _images.cycle_data   = _images.img_results[el.getAttribute('data')];
             _images.cycle_elem   = el;
             _images.cycle_images();
          };
         //if (e.target && e.target.matches("img.modal")){ _scan.modal(e.target);  }
      },



     search:(e)=>{
      _app.el('loading-spinner').style.display = 'block';
      var form = _app.el('search-form');
      var sect = _app.el('section').value;
      var comp = _app.el('company').value;
      var date = _app.el('date').value;
      var fdata = _app.xhr_form_data(form);
      _app.xhr_get('/images/search_sequance', {'section_id':sect,'company_id':comp, 'date':date}, _images.results); //end get
     },


     results:(e)=>{
      var res = _app.xhr_res(e).results;
      _app.el('display-sequence').innerHTML = "";
      for (var k in res){
           _images.get_sequence(res[k].sequence)
      }
      _app.el('loading-spinner').style.display = 'none';

      if (res.length == 0){
       _app.el('display-sequence').innerHTML = "<p>No Results Found</p>";
      }


     },

     cycle_images:() => {
      if (_images.cycle_index >= _images.cycle_data.length){ _images.cycle_index = 0;}
      _images.cycle_elem.src = _images.cycle_data[_images.cycle_index].src_path;
      if (_images.cycle_run){
        _images.time_out = setTimeout((el, d)=>{_images.cycle_images(); _images.cycle_index += 1; }, 1500);
      }

     },

     get_sequence:(seq)=>{
       _app.el('loading-spinner').style.display = 'none';
       _app.xhr_get('/images/get_sequence', {sequence: seq}, _images.display_sequence)
     },

     display_sequence:(e)=> {
      var seq = _app.xhr_res(e).results;
      var img = document.createElement('img');
      _images.img_results[seq[0].sequence] = seq;
      img.title = "View Sequence of "+ seq[0].sequence.split("|").length + " photos";
          img.src = seq[0].thumb_path;
          img.className = 'sm-img sequence pad-img img-layer';
          img.setAttribute('data', seq[0].sequence);
          img.id   = seq[0].id;
       _app.el('display-sequence').appendChild(img);
     },

     slides:{
     idx: 1,
     init:()=>{
      _images.slides.idx = 1;
      _images.slides.divs(_images.slides.idx);
     },

     by_index:(idx)=>{
       _images.slides.idx = idx;
       _images.slides.show(_images.slides.idx);
     },

     divs:(n)=> {
       _images.slides.show(_images.slides.idx += n);
     },


      show:(n)=> {
        var i;
        var x = document.getElementsByClassName("slides");
        if (n > x.length) {_images.slides.idx = 1}
        if (n < 1) {_images.slides.idx = x.length}
        for (i = 0; i < x.length; i++) {
           x[i].style.display = "none";
         }
       x[_images.slides.idx-1].style.display = "block";
     },

     build:(e)=>{
       var seq = e.target.getAttribute('data');
       var res = _images.img_results[seq]
       var tmpl = _.template(_app.el('slide-show-template').innerHTML);
       _app.sleeping_giant._open();
       _app.el('sleeping-giant-body').innerHTML = tmpl({res: res});

     }
}

};
