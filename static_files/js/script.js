function search_submit() {
var username = $("#username").val();
$.getJSON('/checkuseravailability/'+username+"/", 
function(data) {
result = data.result
if (result == "True"){
//$('label[for="fromdate"]').show();
alert("User Name is already registered.")
$('#signupsubmit').attr('disabled','disabled');
}
if (result == "False"){
$("#signupsubmit").removeAttr("disabled");
}});}



function mail_check() {
var email = $("#email").val();
$.getJSON('/checkemailavailability/'+email+"/",
	  
function(data) {
    
result = data.result
if (result == "True"){
alert("Email-address is already registered.")
$('#signupsubmit').attr('disabled','disabled');
}
if (result == "False"){
$("#signupsubmit").removeAttr("disabled");
}});}


function submit_likes() {
var id= parseInt(this.id.replace("likes",""));
var student = $("#student").val();
$.getJSON('/submitlikequestion/'+id+"/"+student+"/", 
function(data) {
result = data.result
already = data.already

alert(already)
});
}


function submit_unlikes() {
var id= parseInt(this.id.replace("unlikes",""));
var student = $("#student").val();
$.getJSON('/submitunlikequestion/'+id+"/"+student+"/", 
function(data) {
result = data.result
});
}




$(document).ready(function () {
    
$("#username").blur(search_submit)
$("#email").blur(mail_check)

$("#[id^='likes']").click(submit_likes)
$("#[id^='unlikes']").click(submit_unlikes)



});





function password_repeat() {
   
var password = $("#password").val();

var cpassword = $("#cpassword").val();
    if (password != cpassword) {
	alert("Password is not matching.")
	$('#signupsubmit').attr('disabled','disabled');
    }
    
    if (password == cpassword) {
	$("#signupsubmit").removeAttr("disabled");
    }
    
}


