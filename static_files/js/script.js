function search_submit() {
var username = $("#username").val();
$.getJSON('/checkuseravailability/'+username+"/", 
function(data) {
result = data.result
if (result == "True"){
$('label[for="fromdate"]').show();
$('#signupsubmit').attr('disabled','disabled');
$('#password').attr('disabled','disabled');
$('#cpassword').attr('disabled','disabled');
$('#email').attr('disabled','disabled');
$('#dob').attr('disabled','disabled');

}
if (result == "False"){
$('label[for="fromdate"]').hide();

$("#signupsubmit").removeAttr("disabled");
$("#password").removeAttr("disabled");
$("#cpassword").removeAttr("disabled");
$("#email").removeAttr("disabled");
$("#dob").removeAttr("disabled");

}});}



function mail_check() {
var email = $("#email").val();
$.getJSON('/checkemailavailability/'+email+"/",
	  
function(data) {
    
result = data.result
if (result == "True"){
$('label[for="email"]').show();
$('#signupsubmit').attr('disabled','disabled');
$('#dob').attr('disabled','disabled');
$('#username').attr('disabled','disabled');

}
if (result == "False"){
$('label[for="email"]').hide();

$("#signupsubmit").removeAttr("disabled");
$("#dob").removeAttr("disabled");
$('#usename').attr('disabled','disabled');

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
	$('label[for="password"]').show();
	$('#username').attr('disabled','disabled');

	$('#signupsubmit').attr('disabled','disabled');
	$('#email').attr('disabled','disabled');
    }
    
    if (password == cpassword) {
	$('label[for="password"]').hide();
	$("#signupsubmit").removeAttr("disabled");
	$("#username").removeAttr("disabled");
	$("#email").removeAttr("disabled");
    }
    
}


