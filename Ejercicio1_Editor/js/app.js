/**
 * NOTA GENERAL:
 * Está solución está más completa de lo que se pedía en las diapositivas.
 * Por ejemplo, se realizan validaciones y se setean valores iniciales en los
 * campos del formulario.
 */

/**
 * VALORES INICIALES:
 * Por defecto, cuando se carga la página, los campos del formulario están
 * vacíos. Opcionalmente, se puede hacer que los campos estén auto-completados.
 * Para ello se hace lo siguiente:
 */
var original_title = $("#content h1").text();
var original_paragraph =
  "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
var original_title_size = $("#content h1").css("font-size").replace("px", "");

$("#title").val(original_title);
$("#paragraph").val(original_paragraph);
$("#fontsize").val(original_title_size);

/* EVENTO CLICK: */
$("#btn-form").on("click", function () {
  // Al clickear, se cierran los alerts que eventualmente puedan estar abiertos:
  $(".alert").alert("close");

  // Se obtienen los valores del formulario al momento de hacer click:
  var titleText = $("#title").val();
  var titleColor = $("input[name=title_color]:checked").val();
  var paragraphText = $("#paragraph").val();
  var fontSize = $("#fontsize").val();

  // Se valida el contenido de los campos:
  if (
    titleColor === "" ||
    titleText === "" ||
    paragraphText === "" ||
    fontSize === ""
  ) {
    // Error: Algún campo está vacío.
    // Se inserta una alerta de error luego del div #content:
    $("#content").after(`
            <div class="alert alert-danger alert-dismissible" role="alert">
                El formulario tiene campos sin completar.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">
                    
                </button>
            </div>
        `);
  } else if (!$.isNumeric(fontSize)) {
    // Error: El campo "Tamaño del título" no contiene un valor numérico.
    // Se inserta una alerta de error luego del div #content:
    $("#content").after(`
      <div class="alert alert-danger alert-dismissible" role="alert">
        Por favor ingresar un número entero para el tamaño del título.
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
    `);
  } else {
    /**
     * No hay errores en el formulario.
     * Se aplica el efecto "slide" al #content.
     * El efecto es opcional.
     */
    $("#content").slideToggle("slow", function () {
      // Código que se ejecuta luego de cerrar #content:

      $("#content h1").css("color", titleColor);
      $("#content h1").text(titleText);
      $("#content p").text(paragraphText);
      $("#content h1").css("font-size", fontSize + "px");

      // Se cierran los alerts que eventualmente puedan estar abiertos.
      $(".alert").alert("close");

      // Se inserta una alerta de éxito luego del div #content:
      $("#content").after(`
        <div class="alert alert-success alert-dismissible fade show" role="alert">
          Los cambios fueron guardados con éxito.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
      `);

      // Se abre el div #content usando efeto "slide":
      $("#content").slideToggle();
    }); // End - Slide Toggle
  }
}); // End - Click en #btn-form
