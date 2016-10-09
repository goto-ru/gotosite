var lock = false;
var slide = 0;
var c = 0;

function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}

function refresh() {
    location.reload();
}

'use strict';

// taken from mo.js demos
function isIOSSafari() {
    var userAgent;
    userAgent = window.navigator.userAgent;
    return userAgent.match(/iPad/i) || userAgent.match(/iPhone/i);
};

// taken from mo.js demos
function isTouch() {
    var isIETouch;
    isIETouch = navigator.maxTouchPoints > 0 || navigator.msMaxTouchPoints > 0;
    return [].indexOf.call(window, 'ontouchstart') >= 0 || isIETouch;
};

// taken from mo.js demos
var isIOS = isIOSSafari(),
    clickHandler = isIOS || isTouch() ? 'touchstart' : 'click';

function extend(a, b) {
    for (var key in b) {
        if (b.hasOwnProperty(key)) {
            a[key] = b[key];
        }
    }
    return a;
}

function Animocon(el, options) {
    this.el = el;
    this.options = extend({}, this.options);
    extend(this.options, options);

    this.checked = false;

    this.timeline = new mojs.Timeline();

    for (var i = 0, len = this.options.tweens.length; i < len; ++i) {
        this.timeline.add(this.options.tweens[i]);
    }

    var self = this;
    this.el.addEventListener(clickHandler, function () {
        if (self.checked) {
            self.options.onUnCheck();
        }
        else {
            self.options.onCheck();
            self.timeline.replay();
        }
        self.checked = !self.checked;
    });
}

Animocon.prototype.options = {
    tweens: [
        new mojs.Burst({})
    ],
    onCheck: function () {
        return false;
    },
    onUnCheck: function () {
        return false;
    }
};



$(window).bind('mousewheel', function (e) {

    if (e.originalEvent.wheelDelta < 100) {
        if (lock == false) {
            if ($('#logo').width() > 300) {
                $('#logo').animate({
                    width: '300px'
                }, 500);
            }
            else {
                lock = true;
            }
        }
        else {
            if (parseInt($('.text').css('top').slice(0, -2)) > ($('#logo').position().top + $('#logo').height() )) {
                $('.text').animate({
                    top: ($('#logo').position().top + $('#logo').height()) + "px"
                }, 500)
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
                    if (c < 30) {
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
                        c = 0;
                    }
                }
            }
        }

    }
    if (e.originalEvent.wheelDelta > 0) {
        if (slide == 1) {
            if (c < 30) {
                c += 1
            }
            else {
                $('.first-slide').animate({
                    top: 0
                }, 2000);

                $('.krutyashki').animate({
                    top: $('.krutyashki').height()
                }, 2000);

                slide = 0;
                c = 0;
            }
        }
        if (slide == 2) {
            if (c < 30) {
                c += 1
            }
            else {
                $('.krutyashki').animate({
                    top: 0
                }, 2000);

                $('.partners').animate({
                    top: $('.partners').height()
                }, 2000);

                slide = 1;
                c = 0;
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
