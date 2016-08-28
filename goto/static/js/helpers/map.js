function load_map(lat, lon, zoom, text) {
    $('#map-outside').toggle();
    $('html').css('overflow', 'hidden');
    var mapProp = {
        center: new google.maps.LatLng(lat, lon),
        zoom: zoom,
        scrollwheel: true,
        navigationControl: false,
        mapTypeControl: false,
        scaleControl: true,
        draggable: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map"), mapProp);
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lon),
        map: map
    });
    if (text.length != 0) {
        var iw1 = new google.maps.InfoWindow({
            content: text
        });
        iw1.open(map, marker);
    }
    google.maps.event.addListener(marker, "click", function (e) {
        iw1.open(map, this);
    });
}

function close_map() {
    $('#map-outside').toggle();
    $('html').css('overflow', 'visible');
}
