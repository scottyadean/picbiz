const _app = {
    csrf_token: '',
    init:function(token){
      this.csrf_token = token;
    },

    xhr_get:function(path, params, callback, rtype='json'){
      var xhr = new XMLHttpRequest();
          xhr.onload = callback;
          xhr.open('GET', path + '?' +_app.query_str(params), true);
          xhr.responseType = rtype;
          xhr.send();
      },
    xhr_post:function(path, params, callback, rtype='json'){
          var data = new FormData();
          data.append('csrfmiddlewaretoken', _app.csrf_token);
          _.forOwn(params, function(v, k) { data.append(k, v); } );

          var xhr = new XMLHttpRequest();
          xhr.open('POST', path, true);
          xhr.onload = callback;
          xhr.responseType = rtype;
          xhr.send(data);
      },
      xhr_res:(e) => {
        return e.target.response;
      },

      event_bind:(root_node, evt_name, callback) => {
          document.getElementById(root_node).addEventListener(evt_name , callback);
      },

      event_add:(el, action, callback)=>{
        el.addEventListener(action, callback);
      },

      event_add_class:(classname, action, callback)=>{
        document.querySelectorAll(classname).forEach(function(element) {
          console.log(element)
          element.addEventListener(action, callback);
        });

      },

      base_name:(str)=>{
        return str.split('\\').pop().split('/').pop();
      },


      query_dom:(q)=>{
        return document.querySelectorAll(q);
      },

      query_str:(obj) =>{
      var str = [];
      for (var p in obj)
        if (obj.hasOwnProperty(p)) {
          str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
        }
      return str.join("&");
    },

    el:function(id){
      return document.getElementById(id);
    },

    el_html:function(el, html){
      el.insertAdjacentHTML('beforeend', html);
    },

    //options tags
    option:{
      create:(id, value) => {
      var option = document.createElement('option');
          option.value = id
          option.text = value;
      return option;
    },
      txt:(el) => {
        if (el.selectedIndex == -1) return null;
        return el.options[el.selectedIndex].text;
      }

    }, //options



};



jQuery(function($) {
  var $bodyEl = $('body'),
      $sidedrawerEl = $('#sidedrawer');


  function showSidedrawer() {
    // show overlay
    var options = {
      onclose: function() {
        $sidedrawerEl
          .removeClass('active')
          .appendTo(document.body);
      }
    };

    var $overlayEl = $(mui.overlay('on', options));

    // show element
    $sidedrawerEl.appendTo($overlayEl);
    setTimeout(function() {
      $sidedrawerEl.addClass('active');
    }, 20);
  }


  function hideSidedrawer() {
    $bodyEl.toggleClass('hide-sidedrawer');
  }


  $('.js-show-sidedrawer').on('click', showSidedrawer);
  $('.js-hide-sidedrawer').on('click', hideSidedrawer);

  // ==========================================================================
  // Animate menu
  // ==========================================================================
  var $titleEls = $('strong', $sidedrawerEl);

  $titleEls
    .next()
    .hide();

  $titleEls.on('click', function() {
    $(this).next().slideToggle(200);
  });


});
