function include(arr, obj) {
    return (arr.indexOf(obj) != -1);
}

$(document).ready(function () {
    // Fucking firefox fix
    $('#logo').css('max-height',$('#text-near-logo').css('height'));
    var a = 0;
    $('.grey-colored').each(function () {
        a += 1;
        if (include(_.range(1, 100, 3), a)) {
            $(this).addClass('green_down');
        }
        if (include(_.range(2, 100, 3), a)) {
            $(this).addClass('orange_down');
        }
        if (include(_.range(3, 100, 3), a)) {
            $(this).addClass('yellow_down');
        }
    });

    a = 0;
    $('.dot').each(function () {
        a += 1;
        if (include(_.range(1, 100, 3), a)) {
            $(this).addClass('green_dot');
        }
        if (include(_.range(2, 100, 3), a)) {
            $(this).addClass('orange_dot');
        }
        if (include(_.range(3, 100, 3), a)) {
            $(this).addClass('yellow_dot');
        }
    });

    var whole_height = 0;
    var count = 1.3;
    var our = 0;
    $('her').each(function () {
        our = parseInt($(this).find('.time-grid').css('height'));
        whole_height += (our / count);
        $(this).find('.space').css('height', our / count);
        $(this).find('.space').children('.dot').css('margin-top', (our / count) / 2);
    });
    var line_height = (whole_height - (our/count)) + our;
    $('.line').css('height', line_height);
});

