// For testing modal delay firing:
// localStorage.clear();

// Adjust the brand text based on window width
$(document).ready(function () {
    if ($(window).width() < 615) {
        $("span.brand").text("FBC");
    } else {
        $("span.brand").text("Federal Bureau of Control");
    }
});

// Adjust the brand text based on window width when the window is resized
$(window).resize(function () {
    if ($(window).width() < 615) {
        $("span.brand").text("FBC");
    } else {
        $("span.brand").text("Federal Bureau of Control");
    }
});

// Enable tooltips for elements with data-toggle="tooltip"
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

// Automatically close the alert message after 3 seconds
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

// Focus on the element with id="myInput" when the modal is shown
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus');
});

// Show the modal if it has not been shown before
$(document).ready(() => {
    console.log(window.localStorage.modal);
    if (window.localStorage.modal != "true") {
        setTimeout(function(){
            $("#myModal").modal('show');
            window.localStorage.modal = true;
        }, 2000);
    }
});