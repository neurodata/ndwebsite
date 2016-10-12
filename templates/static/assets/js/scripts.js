// detect useragent + platform // only when absolutely necessary
var b = document.documentElement;
	b.className = b.className.replace('no-js', 'js');
	b.setAttribute("data-useragent", navigator.userAgent.toLowerCase());
	b.setAttribute("data-platform", navigator.platform.toLowerCase());

var	clStr = b.className,
	ua    = b.getAttribute("data-useragent"),
	pf    = b.getAttribute("data-platform"),
	is    = function(string){ return ua.indexOf(string) > -1 },
	browser = {
		isFirefox : is('firefox'),
		isIE 	  : is('msie') || is('trident/7.0'),
		isIE7 	  : is('msie 7.0'),
		isIE8 	  : is('msie 8.0'),
		isIE9 	  : is('msie 9.0'),
		isIE10 	  : is('msie 10.0'),
		isIE11    : is('rv:11') || is('trident/7.0'),
		isChrome  : is('chrome'),
		isWin7    : is('windows nt 6.1'),
		isWin8    : is('windows nt 6.2'),
		isWindows : pf.indexOf('win32') > -1,
		isAndroid : is('android'),
		isSafari  : is('safari') && !is('chrome'),
		isIPad    : is('ipad'),
		isIPhone  : is('iphone'),
		isAndroid : is('android')
	};
	for ( var title in browser ){
		var helperClass = title.slice(2).toLowerCase();
		if ( browser[title] ) { clStr += helperClass+' '; }
	}
	b.setAttribute('class',clStr);
// end user agent detection

function validEmail(mail) {
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if(mail.match(mailformat))
		return true;
	return false;
}


/*
 __   ___       __      
|__) |__   /\  |  \ \ / 
|  \ |___ /~~\ |__/  |  

*/

function filter(cat) {
	$('#data .grid-25').hide().removeClass('last-2 last-4');
	
	if(cat == 'all') {
		$('#data').removeClass('shuffle');
		$('#data .grid-25').fadeIn('slow');
	} else {
		$('#data').addClass('shuffle').css('opacity',0);
		$('#data .grid-25').filter('.'+cat).show();
		$('#data .grid-25:visible').each(function(i) {
			if((i+1) % 4 == 0) $(this).addClass('last-4');
			if((i+1) % 3 == 0) $(this).addClass('last-3');
			if((i+1) % 2 == 0) $(this).addClass('last-2');
		});
		$('#data').stop().animate({opacity: 1,}, 1500);
	}
}
var cat;

$(document).ready(function() {

// 	if(browser.isIE11 || browser.isIE10 || browser.isIE9){
// 		$('img.wedge').attr('src','/assets/img/wedge-down.png').show();
// 	} else {
// 		$('img.wedge').show();
// 	}

	var body = $('html, body');
		
 	// FastClick
	FastClick.attach(document.body);

	// FitVids
	$('.fitvids').fitVids();
	
	$('.text ol li').each(function(){
		var num = $(this).index() + 1;
		$(this).attr('data-content',num);
	});	
	
	$('#home #data .hovercheck a').hover(
		function(){
			$('#data .mask').stop().animate({opacity: 1}, 'slow');
			$(this).siblings('div').addClass('hovering');
		},
		function(){
			$(this).siblings('div').removeClass('hovering');
			if(!$('.hovercheck').is(':hover')) {
				$('#data .mask').stop().animate({opacity: 0}, 'slow');
			}
		}
	);

	$('a[href="#"]').click(function(e){
		e.preventDefault();
	});

	$('a.menu').click(function(e){
		e.preventDefault();
		if($(this).find('i').is(":visible"))
			$(this).toggleClass('clicked');
	});

	$('a.menu').parent('li').hoverIntent({
		over: overIntent,
		out: outIntent,
		timeout: 250
	});
	function overIntent(){$(this).addClass('hovered');}
	function outIntent(){$(this).removeClass('hovered');}

	$('.team .grid-25').hover(
		function(){
			$(this).addClass('hovered');
			$img = $('img', $(this));
			var imgh = $img.height() + 1;
			$img.siblings('span').css('height',imgh+'px');
		},
		function(){
			$(this).removeClass('hovered');
			$('img', $(this)).siblings('span').css('height','auto');
		}
	);
	
	$('#bottom .grid-3').hover(function(){
		$(this).toggleClass('hovered');
	});
	
	
	$('form input').on('focus', function(){
		$(this).removeClass('error');
	});
	
	
	$('form').on('submit', function(e){
		var errsArr = [];
		var required = $('input[required]', $(this)).serializeArray();
		$.each(required, function(i, field) {
			if(field.value.trim() == '') {
				$('input[name='+field.name+']').addClass('error required');
				errsArr.push({"required":{field: field.name}});
			} else if(field.name == 'emailAddress' &&  !validEmail(field.value)) {
				$('input[name='+field.name+']').addClass('error invalid');
				errsArr.push({"invalid":{field: field.name}});
			}
		});

		if (errsArr.length != 0) {	
			e.preventDefault();
			//alert('test');
			//console.log(errsArr);
		}
	});

	$('#filter.filtering a').on('click', function(){
	
		$filter = $(this).parents('#filter');
	
		if(!$(this).hasClass('selected')) {
			cat = $(this).text().toLowerCase();

			if($(window).width() < 911) {
			
				$filter.removeClass('clicked');
				$('a', $filter).removeClass('show clicked');
				$('a.selected', $filter).html(cat+' <i class="fa fa-bars"></i>');
			
			} else {
				$('a', $filter).removeClass('selected');
				$(this).addClass('selected');
			}
			
			if ($(window).scrollTop() > 0 && $('#ongoing-data').length > 0 ) {
				$('html,body').animate({ scrollTop: 0 }, 'fast', function(){ filter(cat); });
			} else if (!$('#ui-kit').length > 0) {
				filter(cat);			
			}
		} else {
		
			if($(window).width() < 911) {
				$filter.toggleClass('clicked');
				$('a', $filter).addClass('show');
			}
		}
	});

	$('#anchors a').on('click', function(){
		var target = $(this).text().toLowerCase();
		var offset = $('*[data-rel="'+target+'"]').offset();
		$('html,body').animate({ scrollTop: offset.top - 100 }, 'slow');
	});

	$(window).on('load', function() {
	
		if($('#filter').length > 0) {
		
			cat = $('#filter a.selected').text().toLowerCase();
			
			$(window).resize(function(){	
				if(cat != 'all') {
					if($(window).width() < 911) {
						$('#filter a').removeClass('selected');
						$('#filter a.menu').addClass('selected').html(cat+' <i class="fa fa-bars"></i>');
					} else {
						$('#filter a.menu').removeClass('selected').text('All');
						$('#filter a').each(function(){
							if($(this).text().toLowerCase() == cat) {
								$(this).addClass('selected');
							}
						});
					}
				}
			});
		}
		
	});
	
});


$(document).scroll(function(){

	var scroll = $(window).scrollTop();

	if($('video').length > 0) {
		var midpos = $('#midriff').offset();

		if(scroll >= midpos.top){
			$('video').addClass('hide-vid');
		} else {
			$('video').removeClass('hide-vid');
		}
	} else if($('#video').length > 0) {
		var midpos = $('#data').offset();

		if($('#data').length > 0 && scroll >= midpos.top){
			$('#banner').addClass('scrolled');
		} else {
			$('#banner').removeClass('scrolled');
		}
	}	
	
	
	if($('#filter.lockable').length > 0) {
		var filterpos = $('#filter.lockable').offset();
		
		if(!$('#filter.lockable').hasClass('lock')){
			if(scroll >= filterpos.top - 70){
				$('#filter.lockable').addClass('lock');
			}
		} else {
			if(scroll < 70){
				$('#filter.lockable').removeClass('lock');
			}
		}
	}
		
});