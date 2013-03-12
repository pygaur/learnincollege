function search_submit() {
var username = $("#username").val();
$("#username").load("/checkuseravailability/" + encodeURIComponent(username));

//$.getJSON("//" + encodeURIComponent(username), function(data) {
$.get("/checkuseravailability/"+username+"/",
      function(data) {
        alert("Fetched" + data.length + 'items!');
});


return false;
}

$(document).ready(function () {
$("#username").blur(search_submit)


});






