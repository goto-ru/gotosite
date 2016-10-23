var step = 0;

$(document).ready(function () {

    // Copyright by Tvorog
    console.log("Cool designed by Tvorog <https://vk.com/sttrelllok>");

    $("#shariki").width($(document).width);
    var c = document.getElementById("shariki");
    var ctx = c.getContext("2d");
    var cool = new Object();

    top_position = $(".table-shar button").position().top;
    left_position = $(".table-shar button").position().left;
    width = $(".table-shar button").width();
    height = $(".table-shar button").height();

    cool["x1"] = left_position + width / 2 + 5;
    cool["y1"] = top_position + height / 2;
    cool["r1"] = 130;

    cool["x2"] = left_position + width / 2 + 5;
    cool["y2"] = top_position + height / 2;
    cool["r2"] = 130;

    cool["x3"] = left_position + width / 2 + 5;
    cool["y3"] = top_position + height / 2;
    cool["r3"] = 130;


    cool["x4"] = left_position + width / 2 + 5;
    cool["y4"] = top_position + height / 2;
    cool["r4"] = 130;

    cool["x5"] = left_position + width / 2 + 5;
    cool["y5"] = top_position + height / 2;
    cool["r5"] = 130;


    cool["x6"] = left_position + width / 2 + 5;
    cool["y6"] = top_position + height / 2;
    cool["r6"] = 130;
    c.width = window.innerWidth;     // equals window dimension
    c.height = window.innerHeight;

    ctx.lineWidth = 4;

    function draw() {
        setInterval(function () {
            ctx.clearRect(0, 0, c.width, c.height);
            if (step == 0) {
                ctx.beginPath();
                ctx.arc(left_position + width / 2 + 5, top_position + height / 2, 130, 0, 2 * Math.PI, false);
                ctx.stroke();
                ctx.closePath();
            } else if (step == 1) {
                ctx.beginPath();
                ctx.arc(cool["x4"], cool["y4"], cool["r4"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'white';
                ctx.fill();
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool["x5"], cool["y5"], cool["r5"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'white';
                ctx.fill();
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool["x6"], cool["y6"], cool["r6"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'white';
                ctx.fill();
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool["x3"], cool["y3"], cool["r3"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'white';
                ctx.fill();
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool["x2"], cool["y2"], cool["r2"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'white';
                ctx.fill();
                ctx.stroke();
                ctx.closePath();

                ctx.beginPath();
                ctx.arc(cool["x1"], cool["y1"], cool["r1"], 0, 2 * Math.PI, false);
                ctx.fillStyle = 'white';
                ctx.fill();
                ctx.stroke();
                ctx.closePath();
            }
        }, 50);
    }

    draw();

    function rad() {
        function rad1() {
            function rad2() {
                function rad3() {
                    function rad4() {
                        function rad5() {
                            TweenLite.to(cool, 2, {
                                r6: 90,
                                ease: Power4.easeOut
                            });
                        }

                        TweenLite.to(cool, 2, {
                            r5: 70,
                            x6: $('#but6').position().left + 60,
                            y6: $('#but6').position().top + 30,
                            ease: Power4.easeOut,
                            onCompleteParams: rad5()
                        });
                    }

                    TweenLite.to(cool, 2, {
                        r4: 40,
                        x5: $('#but5').position().left + 35,
                        y5: $('#but5').position().top + 30,
                        ease: Power4.easeOut,
                        onCompleteParams: rad4()
                    });
                }

                TweenLite.to(cool, 2, {
                    r3: 120,
                    x4: $('#but4').position().left + 25,
                    y4: $('#but4').position().top + 15,
                    ease: Power4.easeOut,
                    onCompleteParams: rad3()
                });
            }

            TweenLite.to(cool, 2, {
                r2: 80,
                x3: $('#but3').position().left + 95,
                y3: $('#but3').position().top + 35,
                ease: Power4.easeOut,
                onCompleteParams: rad2()
            });
        }

        TweenLite.to(cool, 2, {
            r1: 50,
            x2: $('#but2').position().left + 60,
            y2: $('#but2').position().top + 15,
            ease: Power4.easeOut,
            onCompleteParams: rad1()
        });
    }

    $("#component-2").click(function () {
        $("#component-2").toggle();
        step = 1;
        TweenLite.to(cool, 2, {
            x1: $('#but1').position().left + 30,
            y1: $('#but1').position().top + 10,
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

});
