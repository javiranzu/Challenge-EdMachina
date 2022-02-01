(function ($) {
    'use strict';
    /*==================================================================
        [ Daterangepicker ]*/
    try {
        $('.js-datepicker').daterangepicker({
            "singleDatePicker": true,
            "showDropdowns": true,
            "autoUpdateInput": false,
            locale: {
                format: 'DD/MM/YYYY'
            },
        });

        var myCalendar = $('.js-datepicker');
        var isClick = 0;

        $(window).on('click', function () {
            isClick = 0;
        });

        $(myCalendar).on('apply.daterangepicker', function (ev, picker) {
            isClick = 0;
            $(this).val(picker.startDate.format('DD/MM/YYYY'));

        });

        $('.js-btn-calendar').on('click', function (e) {
            e.stopPropagation();

            if (isClick === 1) isClick = 0;
            else if (isClick === 0) isClick = 1;

            if (isClick === 1) {
                myCalendar.focus();
            }
        });

        $(myCalendar).on('click', function (e) {
            e.stopPropagation();
            isClick = 1;
        });

        $('.daterangepicker').on('click', function (e) {
            e.stopPropagation();
        });


    } catch (er) { console.log(er); }
    /*[ Select 2 Config ]
        ===========================================================*/

    try {
        var selectSimple = $('.js-select-simple');

        selectSimple.each(function () {
            var that = $(this);
            var selectBox = that.find('select');
            var selectDropdown = that.find('.select-dropdown');
            selectBox.select2({
                dropdownParent: selectDropdown
            });
        });

    } catch (err) {
        console.log(err);
    }


})(jQuery);
$( document ).ready(function() {
    materias = []
});

$('#guardar_materia').click(function () {

    if ($("[name='materia']").val() != '' && $("[name='tiempo_cursado']").val() != '' && $("[name='carrera']").val() != '' && $("[name='veces_cursado']").val() != '' && $("#select2-anio_inscripcion-container").text() != 'Año de Inscripción(*)') {


        materia = {
            "materia": $("[name='materia']").val(),
            "tiempo_cursado": $("[name='tiempo_cursado']").val(),
            "carrera": $("[name='carrera']").val(),
            "anio_inscripcion": $("#select2-anio_inscripcion-container").text(),
            "veces_cursado": $("[name='veces_cursado']").val()
        }


        materias.push(materia)
        console.log(materias)

        $("[name='materia']").val('');
        $("[name='tiempo_cursado']").val('');
        $("[name='carrera']").val('');
        $("#select2-anio_inscripcion-container").html('Año de Inscripción(*)');
        $("[name='veces_cursado']").val('');

        materia_html = ''
        i = 0
        materias.forEach(element => {
            console.log(element)
            materia_html = materia_html + '<div class="btn btn--radius btn--yellow" style="cursor:auto; margin-right:2px; margin-bottom:2px;">' + element['materia'] + " " + '<i onclick="eliminar_materia(' + i + ')" class="zmdi zmdi-close imaterias" style="cursor: pointer;"></i>' + '</div>';
            i += 1
        });


        $("#row_materias").html(materia_html);
        $("#error_materia").html(' ');

    } else {

        $("#error_materia").html('Debe completar todos los campos de la materia.');
    }

});

$('#enviar_formulario').click(function () {

    console.log('cantidad materias:' + materias.length)

    emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;

    if ($("[name='nombre']").val() != '' && $("[name='direccion']").val() != '' && $("[name='email']").val() != '' && $("[name='telefono']").val() != '' && materias.length > 0 && emailRegex.test($("[name='email']").val())) {


        request_data = {
            "nombre": $("[name='nombre']").val(),
            "direccion": $("[name='direccion']").val(),
            "email": $("[name='email']").val(),
            "telefono": $("[name='telefono']").val(),
            "materias": materias
        }

        console.log(request_data)
        $.ajax({
            type: "POST",
            url: '/leads',
            contentType: 'application/json;',
            data: JSON.stringify(request_data),
            success: function (data) {
                console.log(data)
                $("[name='nombre']").val('');
                $("[name='direccion']").val('');
                $("[name='email']").val('');
                $("[name='telefono']").val('');

                materias = [];
                materia_html = ''
                i = 0
                materias.forEach(element => {
                    console.log(element)
                    materia_html = materia_html + '<div class="btn btn--radius btn--yellow" style="cursor:auto; margin-right:2px; margin-bottom:2px;">' + element['materia'] + " " + '<i onclick="eliminar_materia(' + i + ')" class="zmdi zmdi-close imaterias" style="cursor: pointer;"></i>' + '</div>';
                    i += 1
                });
                $("#row_materias").html(materia_html);

                $("#sucess_formulario").html(' Registro grabado con éxito. Número de seguimiento de registro:' + data.id_registro);
                $("#error_formulario").html(' ');
                alert('Registro grabado con éxito. Número de seguimiento de registro:' + data.id_registro)

            },
        });


    } else {
        if (materias.length == 0) {
            $("#error_formulario").html('Debe cargar el menos 1 materia.');
        } else if(!(emailRegex.test($("[name='email']").val()))) {
            $("#error_formulario").html('Email incorrecto.');
        } else{
            
            $("#error_formulario").html('Debe completar todos los campos.');
        }

    }

});

