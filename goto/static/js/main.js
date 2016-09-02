$(document).ready(function () {
    if ($(document).width() < 700) {
        $('.todo, .time-col').css('margin', '0 auto');
        $('.white-background, .chel').css('width', '100%');
    }
    $(".navbar-toggle").click(function () {
        $('body').animate({right: '150'}, 500);
        $('.mobile-sheet').toggle().animate({right: '0'}, 500);
    });

    if ($('.much').length > 4) {
        $('.much').css('display', 'none');
        $('.much:eq( 0 )').toggle();
        $('.much:eq( 1 )').toggle();
        $('.much:eq( 2 )').toggle();
        $('.much:eq( 3 )').toggle();
        // $('.much:eq( 4 )').toggle();
        // $('.much:eq( 5 )').toggle();
        // $('.much:eq( 6 )').toggle();
        // $('.much:eq( 7 )').toggle()
    }
    else {
        $('.togmuch').toggle();
    }
});

function took() {
    $('.much').css('display', 'none').toggle();
    $('.togmuch').toggle();
}

function close_message(obj) {
    $(obj).css('display', 'none')
}
