function edit() {
    $('.profileedit').toggle();

    $('iframe').height($('iframe').contents().find('.row').height());

    $('.profil-base').toggle();

    $('#kik').contents().find('input:submit').click(function () {
        location.reload()
    })
}
