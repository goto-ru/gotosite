function load_orange() {
    $('link').remove('.green-css');
    $('head')
        .append('<link class="orange-css" rel="stylesheet" href="/static/css/schools/school_first.css" type="text/css" />');

}

function load_green() {
    $("link").remove(".orange-css");
    $('head')
        .append('<link class="green-css" rel="stylesheet" href="/static/css/schools/school_second.css" type="text/css" />');
}
