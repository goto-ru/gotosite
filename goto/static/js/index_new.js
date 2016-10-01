var lock = false;
var slide = 0;
var c = 0;

function refresh() {
    location.reload();
}

$(window).bind('mousewheel', function (e) {

    if (e.originalEvent.wheelDelta < 100) {
        if (lock == false) {
            if ($('#logo').width() > 430) {
                $('#logo').animate({
                    width: '-=10px'
                }, 1);
            }
            else {
                lock = true;
            }
        }
        else {
            if (parseInt($('.text').css('top').slice(0, -2)) > ($('#logo').position().top + $('#logo').height() )) {
                $('.text').animate({
                    top: '-=10px'
                }, 0.000001)
            }
            else {
                if (slide == 0) {
                    $('.first-slide').animate({
                        top: (0 - $('.first-slide').height() - 30)
                    }, 2000);

                    $('.krutyashki').animate({
                        top: 0
                    }, 2000);

                    slide = 1;
                    c = 0;
                }

                if (slide == 1) {
                    if (c < 10) {
                        c += 1
                    }
                    else {
                        $('.krutyashki').animate({
                            top: (0 - $('.krutyashki').height() - 30)
                        }, 2000);

                        $('.partners').animate({
                            top: 0
                        }, 2000);

                        slide = 2;
                        c = 0
                    }
                }
            }
        }

    }
    if (e.originalEvent.wheelDelta > 0) {

        if (slide == 1) {
            $('.first-slide').animate({
                top: 0
            }, 2000);

            $('.krutyashki').animate({
                top: $('.krutyashki').height()
            }, 2000);

            slide = 0;
        }
        if (slide == 2) {
            $('.krutyashki').animate({
                top: 0
            }, 2000);

            $('.partners').animate({
                top: $('.partners').height()
            }, 2000);

            slide = 2;
        }
    }

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
