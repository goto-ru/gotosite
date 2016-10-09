var up = 0;
var down = 0;
var slide = 0;

var lock = false;

function next_down() {
    slide += 1;
}

function next_up() {
    slide -= 1;
}

function get_slide(n) {
    if (lock == false) {
        if (n == 0) {
            console.log('first slide');


            lock = true;
            $('#logo').animate({'width': '479px'}, 1000);
            $('.text').animate({top: '100vh'}, 1000);

            setTimeout(function () {
                lock = false;
            }, 1000);
        }

        else if (n == 1) {
            console.log('second slide');


            lock = true;
            $('#logo').animate({'width': '300px'}, 1000);
            $('.text').animate({top: $('#logo').position().top + 260 + 'px'}, 1000);

            setTimeout(function () {
                lock = false;
            }, 1000);
        }
        else if (n == 2) {

        }
    }
    else {
        return 0;
    }
}

$(window).bind('mousewheel', function (e) {
    if (e.originalEvent.wheelDelta < 0) {
        down += 1;
        if (down > 1) {
            down = 0;
            if (get_slide(slide + 1) != 0){
                next_down();
            }
        }
    }
    else {
        up += 1;
        if (up > 1) {
            up = 0;
            if (get_slide(slide -= 1) != 0){
                next_up();
            }
        }
    }
});

$(document).ready(function (ev) {
    var toggle = $('#ss_toggle');
    var menu = $('#ss_menu');
    var rot;

    $('#ss_toggle').on('click', function (ev) {
        rot = parseInt($(this).data('rot')) - 180;
        menu.css('transform', 'rotate(' + rot + 'deg)');
        menu.css('webkitTransform', 'rotate(' + rot + 'deg)');
        if ((rot / 180) % 2 == 0) {
            //Moving in
            toggle.parent().addClass('ss_active');
            toggle.addClass('close');
        } else {
            //Moving Out
            toggle.parent().removeClass('ss_active');
            toggle.removeClass('close');
        }
        $(this).data('rot', rot);
    });

    menu.on('transitionend webkitTransitionEnd oTransitionEnd', function () {
        if ((rot / 180) % 2 == 0) {
            $('#ss_menu div i').addClass('ss_animate');
        } else {
            $('#ss_menu div i').removeClass('ss_animate');
        }
    });

});

function cool(i) {
    $('.opisanie').css('display', 'block').css('bottom', '0').css('height', '320');

    if (i == 0) {
        $('.opisanie').css('background-color', 'rgb(81, 13, 129)');
        $('.programm-text').css('display', 'none');
        $('.ad-text').css('display', 'none');
        $('.bio-text').css('display', 'none');
        $('.robot-text').css('display', 'block');
    }
    if (i == 1) {
        $('.opisanie').css('background-color', 'rgb(67, 180, 152)');
        $('.robot-text').css('display', 'none');
        $('.ad-text').css('display', 'none');
        $('.bio-text').css('display', 'none');
        $('.programm-text').css('display', 'block');
    }
}

function ntcool(i) {
    $('.opisanie').css('display', 'block');

    if (i == 2) {
        $('.opisanie').css('background-color', 'rgb(238, 229, 58)');
        $('.programm-text').css('display', 'none');
        $('.ad-text').css('display', 'block');
        $('.bio-text').css('display', 'none');
        $('.robot-text').css('display', 'none');
    }
    if (i == 3) {
        $('.opisanie').css('background-color', 'rgb(255, 140, 102)');
        $('.robot-text').css('display', 'none');
        $('.ad-text').css('display', 'none');
        $('.bio-text').css('display', 'block');
        $('.programm-text').css('display', 'none');
    }
}

function awesome() {
    $('.opisanie').toggle().css('bottom', '').css('height', '305');
    $('.robot-text').css('display', 'none');
    $('.programm-text').css('display', 'none');
    $('.ad-text').css('display', 'none');
    $('.bio-text').css('display', 'none');
}
