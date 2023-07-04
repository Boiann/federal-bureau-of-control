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
    $('[data-toggle="tooltip"]').tooltip()
})

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);