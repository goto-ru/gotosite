function load_orange() {
    $('link').remove('.green-css');
    $('head')
        .append( $('<link class="orange-css" rel="stylesheet" type="text/css" />')
            .attr('href', '/static/css/schools/school_first.css') );
}

function load_green() {
    $("link").remove(".orange-css");
    $('head')
        .append( $('<link class="green-css" rel="stylesheet" type="text/css" />')
            .attr('href', '/static/css/schools/school_second.css') );
}
