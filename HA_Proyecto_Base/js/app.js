$(".btn-primary").on("click", function() {
    var titulo = $("#titulo").val();
    console.log(titulo)
    if (titulo !== "") {
        $("h2").text(titulo);
    }
    var parrafo = $("#parrafo").val();
    if (parrafo) {
        $("p").text(parrafo);
    }

    var color = $("input[name=titulo-color]:checked").val();

    $("h2").css("color", color);

    var tamano = $("#tamano-de-letra").val();
    $("h2").css("font-size", tamano + "px");

    if (parrafo && color && tamano && titulo) {
        $("#alerta-success").show();
    }

})