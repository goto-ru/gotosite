$(document).ready(function () {
    // Copyright by Tvorog
    console.log("Cool designed by Tvorog <https://vk.com/sttrelllok>");

    $("#shariki").width($(document).width);
    var c = document.getElementById("shariki");
    var ctx = c.getContext("2d");
    var cool = new Object();
    cool["x"] = 0;
    cool["y"] = 0;
    cool["x_biggest"] = 0;
    cool["y_biggest"] = 0;

    c.width = window.innerWidth;     // equals window dimension
    c.height = window.innerHeight;


    top_position = $(".table-shar button").position().top;
    left_position = $(".table-shar button").position().left;
    width = $(".table-shar button").width();
    height = $(".table-shar button").height();

    ctx.lineWidth = 4;


    ctx.stroke();


    ctx.stroke();

    function draw() {
        setInterval(function () {
            stop = false;

            if (stop == false) {
                ctx.clearRect(0, 0, c.width, c.height);
                ctx.beginPath();

                // Верхняя
                if (cool["y_biggest"] != 30 && cool["x_biggest"] != width + 68) {
         ctx.moveTo(left_position - 80, top_position);
                ctx.bezierCurveTo(
                    left_position - 40 - cool["y_biggest"], top_position - cool["x_biggest"],
                    left_position + width + 40 + cool["y_biggest"], top_position - cool["x_biggest"],
                    left_position + width + 80, top_position);
                } else {
                    ctx.arc(left_position + width / 2, top_position, width + 25, Math.PI, 2 * Math.PI);
                }

                // Нижняя

               ctx.moveTo(left_position - 80, top_position + height);
                    ctx.bezierCurveTo(
                        left_position - 40 - cool["y_biggest"], top_position + height + cool["x_biggest"],
                        left_position + width + 40 + cool["y_biggest"], top_position + height + cool["x_biggest"],
                        left_position + width + 80, top_position + height);
                // Левая
                ctx.moveTo(left_position - 79, top_position);
                ctx.bezierCurveTo(
                    left_position - 79 - cool["x"], top_position + height / 2 - cool["y"],
                    left_position - 79 - cool["x"], top_position + height / 2 + cool["y"],
                    left_position - 79, top_position + height);

                // Правая
                ctx.moveTo(left_position + width + 79, top_position);
                ctx.bezierCurveTo(
                    left_position + width + 79 + cool["x"], top_position + height / 2 - cool["y"],
                    left_position + width + 79 + cool["x"], top_position + height / 2 + cool["y"],
                    left_position + width + 79, top_position + height);

                ctx.stroke();
                ctx.closePath();
            }
        }, 50);


    }

    draw();


    $("#component-2").click(function () {
        TweenLite.to(cool, 2, {x: 100, x_biggest: width + 68, y_biggest: 30, y: 30, ease: Bounce.easeInOut});
    });

});
