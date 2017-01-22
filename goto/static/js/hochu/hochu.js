var step = 0;
var cool_clas = new Object();
var l = 138;
var ll = 110;

$("#shariki").width($(document).width);
var c = document.getElementById("shariki");
var ctx = c.getContext("2d");

$(document).ready(function () {

    top_position = $(".table-shar button").position().top;
    left_position = $(".table-shar button").position().left;
    width = $(".table-shar button").width();
    height = $(".table-shar button").height();

    locked_f = false;
    lock_click = false;

    cool_clas["x1"] = left_position + width / 2 + 98;
    cool_clas["y1"] = top_position + height / 2 + 98;
    cool_clas["r1"] = 130;

    cool_clas["x2"] = left_position + width / 2 + 98;
    cool_clas["y2"] = top_position + height / 2 + 98;
    cool_clas["r2"] = 130;

    cool_clas["x3"] = left_position + width / 2 + 98;
    cool_clas["y3"] = top_position + height / 2 + 98;
    cool_clas["r3"] = 130;


    cool_clas["x4"] = left_position + width / 2 + 98;
    cool_clas["y4"] = top_position + height / 2 + 98;
    cool_clas["r4"] = 130;

    cool_clas["x5"] = left_position + width / 2 + 98;
    cool_clas["y5"] = top_position + height / 2 + 98;
    cool_clas["r5"] = 130;


    cool_clas["x6"] = left_position + width / 2 + 98;
    cool_clas["y6"] = top_position + height / 2 + 98;
    cool_clas["r6"] = 130;

    cool_clas["line_helper"] = 4;
    c.width = window.innerWidth;     // equals window dimension
    c.height = window.innerHeight;

    ctx.lineWidth = 4;

    function draw() {
        setInterval(function () {
            ctx.clearRect(0, 0, c.width, c.height);
            if (step == 0) {
                ctx.beginPath();
                ctx.arc(left_position + width / 2 + 98, top_position + height / 2 + 98, 130, 0, 2 * Math.PI, false);
                ctx.strokeStyle = '#080808';
                ctx.stroke();
                ctx.closePath();
            } else if (step == 1) {
                ctx.lineWidth = cool_clas["line_helper"];

                ctx.beginPath();
                ctx.moveTo(cool_clas["x4"], cool_clas["y4"]);
                ctx.lineTo(cool_clas["x5"], cool_clas["y5"]);
                ctx.strokeStyle = 'rgba(97,97,97,0.5)';
                ctx.stroke();

                ctx.beginPath();
                ctx.moveTo(cool_clas["x6"], cool_clas["y6"]);
                ctx.lineTo(cool_clas["x5"], cool_clas["y5"]);
                ctx.strokeStyle = 'rgba(97,97,97,0.5)';
                ctx.stroke();

                ctx.beginPath();
                ctx.moveTo(cool_clas["x6"], cool_clas["y6"]);
                ctx.lineTo(cool_clas["x2"], cool_clas["y2"]);
                ctx.strokeStyle = 'rgba(97,97,97,0.5)';
                ctx.stroke();


                ctx.beginPath();
                ctx.moveTo(cool_clas["x1"], cool_clas["y1"]);
                ctx.lineTo(cool_clas["x3"], cool_clas["y3"]);
                ctx.strokeStyle = 'rgba(97,97,97,0.5)';
                ctx.stroke();

                ctx.beginPath();
                ctx.moveTo(cool_clas["x3"], cool_clas["y3"]);
                ctx.lineTo(cool_clas["x2"], cool_clas["y2"]);
                ctx.strokeStyle = 'rgba(97,97,97,0.5)';
                ctx.stroke();


                ctx.lineWidth = 4;

                ctx.beginPath();
                ctx.arc(cool_clas["x4"], cool_clas["y4"], cool_clas["r4"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(67, 180, 152)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(67, 180, 152)';
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool_clas["x5"], cool_clas["y5"], cool_clas["r5"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(255, 140, 102)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(255, 140, 102)';
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool_clas["x6"], cool_clas["y6"], cool_clas["r6"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(81, 13, 129)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(81, 13, 129)';
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool_clas["x3"], cool_clas["y3"], cool_clas["r3"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(255, 140, 102)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(255, 140, 102)';
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool_clas["x2"], cool_clas["y2"], cool_clas["r2"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(67, 180, 152)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(67, 180, 152)';
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool_clas["x1"], cool_clas["y1"], cool_clas["r1"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(81, 13, 129)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(81, 13, 129)';
                ctx.stroke();
                ctx.closePath();
            } else if (step == 2) {
            } else if (step == 3) {

                ctx.beginPath();
                ctx.arc($('#but3').position().left + 138, $('#but3').position().top + 110, cool_clas["r3"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(255, 140, 102)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(255, 140, 102)';
                ctx.stroke();
                ctx.closePath();

            } else if (step == 4) {

                $('.take_part_in').each(function () {
                    ctx.beginPath();
                    ctx.moveTo($('#but3').position().left + 138, $('#but3').position().top + 110);
                    ctx.lineTo(c.width / 2, $(this).position().top + 60);
                    ctx.strokeStyle = 'rgba(97,97,97,0.5)';
                    ctx.stroke();
                });


                ctx.beginPath();
                ctx.arc($('#but3').position().left + 138, $('#but3').position().top + 110, cool_clas["r3"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'rgb(255, 140, 102)';
                ctx.fill();
                ctx.strokeStyle = 'rgb(255, 140, 102)';
                ctx.stroke();
                ctx.closePath();

            }
        }, 10);
    }

    draw();

    function rad() {
        function rad1() {
            function rad2() {
                function rad3() {
                    function rad4() {
                        function rad5() {
                            TweenLite.to(cool_clas, 2, {
                                r6: 80,
                                ease: Power4.easeOut
                            });
                        }

                        TweenLite.to(cool_clas, 2, {
                            r5: 68,
                            x6: $('#but6').position().left + 100, // новости
                            y6: $('#but6').position().top + 60,
                            ease: Power4.easeOut,
                            onCompleteParams: rad5()
                        });
                    }

                    TweenLite.to(cool_clas, 2, {
                        r4: 90,
                        x5: $('#but5').position().left + 88, // подробности о проекте
                        y5: $('#but5').position().top + 57,
                        ease: Power4.easeOut,
                        onCompleteParams: rad4()
                    });
                }

                TweenLite.to(cool_clas, 2, {
                    r3: 120,
                    x4: $('#but4').position().left + 99, // преподавать
                    y4: $('#but4').position().top + 43,
                    ease: Power4.easeOut,
                    onCompleteParams: rad3()
                });
            }

            TweenLite.to(cool_clas, 2, {
                r2: 100,
                x3: $('#but3').position().left + 138, //принять участие
                y3: $('#but3').position().top + 110,
                ease: Power4.easeOut,
                onCompleteParams: rad2()
            });
        }

        TweenLite.to(cool_clas, 2, {
            r1: 60,
            x2: $('#but2').position().left + 113, // стать партнёром
            y2: $('#but2').position().top + 80,
            ease: Power4.easeOut,
            onCompleteParams: rad1()
        });
    }

    $("#component-2").click(function () {
        $("#component-2").toggle();
        $(".back-hochu").toggle();
        step = 1;
        TweenLite.to(cool_clas, 2, {
            x1: $('#but1').position().left + 90, // подписаться
            y1: $('#but1').position().top + 50,
            ease: Power4.easeOut,
            onCompleteParams: rad()
        });
        setTimeout(function () {
            $('#but1').css('color', 'black');
            $('#but1').css('z-index', '200');

            $('#but2').css('color', 'black');
            $('#but2').css('z-index', '200');

            $('#but3').css('color', 'black');
            $('#but3').css('z-index', '200');

            $('#but4').css('color', 'black');
            $('#but4').css('z-index', '200');

            $('#but5').css('color', 'black');
            $('#but5').css('z-index', '200');

            $('#but6').css('color', 'black');
            $('#but6').css('z-index', '200');
        }, 1200)

    });

    $('#but1').mouseenter(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r1: 80,
                ease: Power4.easeOut
            });
        }
    });

    $('#but1').mouseout(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r1: 60,
                ease: Power4.easeOut
            });
        }
    });


    $('#but2').mouseenter(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r2: 120,
                ease: Power4.easeOut
            });
        }
    });

    $('#but2').mouseout(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r2: 100,
                ease: Power4.easeOut
            });
        }
    });


    $('#but3').mouseenter(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r3: 140,
                ease: Power4.easeOut
            });
        }
    });

    $('#but3').mouseout(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r3: 120,
                ease: Power4.easeOut
            });
        }
    });


    $('#but4').mouseenter(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r4: 110,
                ease: Power4.easeOut
            });
        }
    });

    $('#but4').mouseout(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r4: 90,
                ease: Power4.easeOut
            });
        }
    });


    $('#but5').mouseenter(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r5: 88,
                ease: Power4.easeOut
            });
        }
    });

    $('#but5').mouseout(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r5: 68,
                ease: Power4.easeOut
            });
        }
    });


    $('#but6').mouseenter(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r6: 90,
                ease: Power4.easeOut
            });
        }
    });

    $('#but6').mouseout(function () {
        if (locked_f == false) {
            TweenLite.to(cool_clas, 2, {
                r6: 80,
                ease: Power4.easeOut
            });
        }
    });


});

function come_to_us_brother() {
    locked_f = true;

    TweenLite.to(cool_clas, 2, {
        line_helper: 0,
        r4: 0,
        r3: 0,
        r5: 0,
        r6: 0,
        r2: 0,
        r1: 0,
        ease: Power4.easeOut
    });

    setTimeout(function () {
        step = 2;
        $("#but1").css('display', 'none');
        $("#but2").css('display', 'none');
        $("#but3").css('display', 'none');
        $("#but4").css('display', 'none');
        $("#but5").css('display', 'none');
        $("#but6").css('display', 'none');
        locked_f = false;

        $('#come_to_us_brother').toggle();
    }, 1000);
}


$(".back-hochu").click(function () {
    if (step == 1) {
        $(".back-hochu").toggle();
        $("#but1").css('display', 'none');
        $("#but2").css('display', 'none');
        $("#but3").css('display', 'none');
        $("#but4").css('display', 'none');
        $("#but5").css('display', 'none');
        $("#but6").css('display', 'none');

        TweenLite.to(cool_clas, 2, {
            line_helper: 0,
            r4: 0,
            r5: 0,
            r6: 0,
            r3: 0,
            r2: 0,
            r1: 0,
            ease: Power4.easeOut
        });

        setTimeout(function () {
            step = 0;
            $("#component-2").toggle();

            cool_clas["x1"] = left_position + width / 2 + 98;
            cool_clas["y1"] = top_position + height / 2 + 98;
            cool_clas["r1"] = 130;

            cool_clas["x2"] = left_position + width / 2 + 98;
            cool_clas["y2"] = top_position + height / 2 + 98;
            cool_clas["r2"] = 130;

            cool_clas["x3"] = left_position + width / 2 + 98;
            cool_clas["y3"] = top_position + height / 2 + 98;
            cool_clas["r3"] = 130;


            cool_clas["x4"] = left_position + width / 2 + 98;
            cool_clas["y4"] = top_position + height / 2 + 98;
            cool_clas["r4"] = 130;

            cool_clas["x5"] = left_position + width / 2 + 98;
            cool_clas["y5"] = top_position + height / 2 + 98;
            cool_clas["r5"] = 130;


            cool_clas["x6"] = left_position + width / 2 + 98;
            cool_clas["y6"] = top_position + height / 2 + 98;
            cool_clas["r6"] = 130;

            cool_clas["line_helper"] = 4;
        }, 1000);

    }
});

function take_part() {
    if (lock_click == false) {
        locked_f = true;

        TweenLite.to(cool_clas, 2, {
            line_helper: 0,
            r4: 0,
            r5: 0,
            r6: 0,
            r2: 0,
            r1: 0,
            ease: Power4.easeOut
        });

        setTimeout(function () {
            step = 3;
            $("#but1").css('display', 'none');
            $("#but2").css('display', 'none');
            $("#but4").css('display', 'none');
            $("#but5").css('display', 'none');
            $("#but6").css('display', 'none');
            locked_f = false;

            $('#but3').animate({
                top: $('.take_part_in').position().top + 200,
                left: "20vw"
            }, 1000);

            step = 4;
            lock_click = true;
            $('#take-part').toggle();
        }, 1000);
    }
}

$('.input').keypress(function (e) {
    if (e.which == 13 && step == 2) {
        alert($('#come_to_us_brother input').val());

        $('#come_to_us_brother').toggle();

        step = 0;
        $("#component-2").toggle();
        $("#want").toggle();
        $(".subscription_alert").toggle();


        cool_clas["x1"] = left_position + width / 2 + 98;
        cool_clas["y1"] = top_position + height / 2 + 98;
        cool_clas["r1"] = 130;

        cool_clas["x2"] = left_position + width / 2 + 98;
        cool_clas["y2"] = top_position + height / 2 + 98;
        cool_clas["r2"] = 130;

        cool_clas["x3"] = left_position + width / 2 + 98;
        cool_clas["y3"] = top_position + height / 2 + 98;
        cool_clas["r3"] = 130;


        cool_clas["x4"] = left_position + width / 2 + 98;
        cool_clas["y4"] = top_position + height / 2 + 98;
        cool_clas["r4"] = 130;

        cool_clas["x5"] = left_position + width / 2 + 98;
        cool_clas["y5"] = top_position + height / 2 + 98;
        cool_clas["r5"] = 130;


        cool_clas["x6"] = left_position + width / 2 + 98;
        cool_clas["y6"] = top_position + height / 2 + 98;
        cool_clas["r6"] = 130;

        cool_clas["line_helper"] = 4;

        step = 0;
        setTimeout(function () {
            $(".subscription_alert").toggle();
            $("#want").toggle();

            cool_clas["x1"] = left_position + width / 2 + 98;
            cool_clas["y1"] = top_position + height / 2 + 98;
            cool_clas["r1"] = 130;

            cool_clas["x2"] = left_position + width / 2 + 98;
            cool_clas["y2"] = top_position + height / 2 + 98;
            cool_clas["r2"] = 130;

            cool_clas["x3"] = left_position + width / 2 + 98;
            cool_clas["y3"] = top_position + height / 2 + 98;
            cool_clas["r3"] = 130;


            cool_clas["x4"] = left_position + width / 2 + 98;
            cool_clas["y4"] = top_position + height / 2 + 98;
            cool_clas["r4"] = 130;

            cool_clas["x5"] = left_position + width / 2 + 98;
            cool_clas["y5"] = top_position + height / 2 + 98;
            cool_clas["r5"] = 130;


            cool_clas["x6"] = left_position + width / 2 + 98;
            cool_clas["y6"] = top_position + height / 2 + 98;
            cool_clas["r6"] = 130;
        }, 1000);
    }
});
