
var lastChecked = null;

var select_on_shift = (dom_el, selector) => {

  $(dom_el).delegate(selector, 'click', function(e) {
      var $chkboxes = $(selector);
      if(!lastChecked) {
          lastChecked = this;
          return;
      }
      if(e.shiftKey) {
          var start = $chkboxes.index(this);
          var end   = $chkboxes.index(lastChecked);
          $chkboxes.slice(Math.min(start,end), Math.max(start,end)+ 1).prop('checked', lastChecked.checked);
      }
      lastChecked = this;
    });

  };
