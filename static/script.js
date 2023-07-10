// For testing modal delay firing:
// localStorage.clear();

$(document).ready(function () {
    if ($(window).width() < 615) {
        $("span.brand").text("FBC");
    } else {
        $("span.brand").text("Federal Bureau of Control");
    }
});

$(window).resize(function () {
    if ($(window).width() < 615) {
        $("span.brand").text("FBC");
    } else {
        $("span.brand").text("Federal Bureau of Control");
    }
});

$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus');
});

$(document).ready(() => {
    console.log(window.localStorage.modal);
    if (window.localStorage.modal != "true") {
        setTimeout(function(){
            $("#myModal").modal('show');
            window.localStorage.modal = true;
        }, 2000);
    }
});