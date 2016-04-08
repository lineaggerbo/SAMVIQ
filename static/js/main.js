//window.onbeforeunload = function(e) {
//  return 'Dialog text here.';
//};



function checkAllInput(){
  if ($('#navigation ul li.scored').length == $('#navigation ul li').length) {
    $('.next-scene').removeClass('button-disabled');
  };
}

function shuffleTabs(){
  var tab_names = [];

  // Extract and remove data tab reference
  $('#navigation ul li:not(:first)').each(function(i,val){
    tab_names[i] = $(this).data('tab');
  });

  // Shuffle tab references
  for (var i = tab_names.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = tab_names[i];
    tab_names[i] = tab_names[j];
    tab_names[j] = temp;
  }

  // Assign each link with new reference
  $('#navigation ul li:not(:first)').each(function(i,val){
       $(this).attr('data-tab',tab_names[i]);
       var id = tab_names[i].match(/\d+/); 
       $(this).find("input").attr('name', "score-" + id);
  });
}

$(document).ready(function(){

  var tab_current = 'tab-ref';

  shuffleTabs();

  $('.tab-link').click(function(){
    var tab_id = $(this).attr('data-tab');
    tab_current = tab_id;
    $('.tab-content').removeClass('tab-current');
    $('#'+tab_id).addClass('tab-current');
    $('.tab-link').removeClass('button-current');
    $(this).addClass('button-current');
  });

  $('.rating').each(function(){
    $('.slider', $(this)).slider({
      orientation: "vertical",
      range: "min",
      min: 0,
      max: 100,
      value: 50,
      slide: function(event, ui){
        $(this).parent().find('.score').val(ui.value);
        $('#navigation ul li[data-tab='+tab_current+'] input').val(ui.value);
        $('#navigation ul li[data-tab='+tab_current+']').addClass('scored');
        checkAllInput();
      }
    });
    $('.score').val($('.slider').slider("value"));
  });

});



