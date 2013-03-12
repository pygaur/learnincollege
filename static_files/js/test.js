$(document).ready(function(){ 
    //attach a jQuery live event to the button
    //$('#getdata-button').live('click', function(){
        //console.log("echo ")
        $.getJSON("test.html", function(data) {
        console.log("echo "+ data)
            //alert(data); //uncomment this for debug
            //alert (data.item1+" "+data.item2+" "+data.item3); //further debug
            $('#test').html("<p>teste="+data.result+"</p>");
        });
    });
//});