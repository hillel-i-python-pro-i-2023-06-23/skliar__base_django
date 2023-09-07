document.addEventListener("DOMContentLoaded", function() {
    const showButton = document.getElementById("showButton");
    const myForm = document.getElementById("myForm");
    showButton.addEventListener("click", function() {
        myForm.style.display = "block";

    });
});
