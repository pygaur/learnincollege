function search_submit() {
var username = $("#username").val();

    $.getJSON('/checkuseravailability/'+username+"/", 
    function(data) {
        result = data.result
        if (result == "True"){
         	$('label[for="fromdate"]').show();

        }
        if (result == "False"){
            	$('label[for="fromdate"]').hide();

        }
        
        
    });

}



function submit_likes() {
    
var id= parseInt(this.id.replace("likes",""));

var student = $("#student").val();

    $.getJSON('/submitlikequestion/'+id+"/"+student+"/", 
    function(data) {
        result = data.result
        
        
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

$("#[id^='likes']").click(submit_likes)
$("#[id^='unlikes']").click(submit_unlikes)



});






