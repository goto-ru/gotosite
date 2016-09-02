function edit() {
    $('.profileedit').toggle();

    $('iframe').height($('iframe').contents().find('.row').height());

    $('.profil-base').toggle();

    $('#kik').contents().find('input:submit').click(function () {
        location.reload()
    })
}

$(document).ready(function () {
    var example4 = new Taggle('example4');
    var container = example4.getContainer();
    var input = example4.getInput();

    $(input).autocomplete({
        source: ['Творожков Андрей', 'Васильев Олег', 'Алёна Ильина', 'Шунин Тимофей'], // See jQuery UI documentaton for options
        appendTo: container,
        position: {at: "left bottom", of: container},
        select: function (event, data) {
            event.preventDefault();
            //Add the tag if user clicks
            if (event.which === 1) {
                example4.add(data.item.value);
            }
        }
    });

    $('.taggle_input').attr('placeholder', 'Участники (начните вводить имя)')
});

$('#project-image').click(function(){ $('#imgupload').trigger('click'); });
