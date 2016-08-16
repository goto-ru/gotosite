$(document).ready(function () {
    if ($(document).width() < 700) {
        $('.todo, .time-col').css('margin', '0 auto');
        $('.white-background, .chel').css('width', '100%');
    }
    $(".navbar-toggle").click(function () {
        $('body').animate({right:'150'}, 500);
        $('.mobile-sheet').toggle().animate({right:'0'}, 500);
    });
});
