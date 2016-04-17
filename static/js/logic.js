var drinkName = "";
var drinkSize = 0;
var drinkOrder = [];

$(document).ready(function() {
	$("#warning").hide();
	$('#romCoke').click(function() {
		drinkName = "romCoke";
		$(this).animate({opacity:0.5}, 1000);
		$('#ginTonic').animate({opacity:1}, 1000);
		$('#vodkaFanta').animate({opacity:1}, 1000);
		check();
	})

	$('#ginTonic').click(function() {
		drinkName = "ginTonic";
		$(this).animate({opacity:0.5}, 1000);
		$('#romCoke').animate({opacity:1}, 1000);
		$('#vodkaFanta').animate({opacity:1}, 1000);
		check();
	})

	$('#vodkaFanta').click(function() {
		drinkName = "vodkaFanta";
		$(this).animate({opacity:0.5}, 1000);
		$('#romCoke').animate({opacity:1}, 1000);
		$('#ginTonic').animate({opacity:1}, 1000);
		check();
	})

	$('#40').click(function() {
		drinkSize = 40;
		check();
	})

	$('#200').click(function() {
		drinkSize = 200;
		check();
	})

	$('#400').click(function() {
		drinkSize = 400;
		check();
	})

	$('#mix').click(function() {
		drinkOrder = [drinkName, drinkSize];
		$('#ginTonic').animate({opacity:1}, 1000);
		$('#romCoke').animate({opacity:1}, 1000);
		$('#vodkaFanta').animate({opacity:1}, 1000);
		console.log("WTF! " + drinkSize + " " + drinkName)


		var data = {
			name: drinkName,
			size: drinkSize
		};

		$.ajax({
			type: 'POST',
			url: window.location.href,
			data: JSON.stringify(data),
			dataType: 'json',
			contentType: 'application/json; charset=utf-8'
		}).done(function(msg) {
			alert("Data Saved: " + msg);
		});


		drinkSize = 0;
		drinkName = "";
	})
});

function check() {
	if (drinkSize != 0 && drinkName != "") {
		$('#mix').removeAttr('disabled');
	}
}

var counter = 0;  
var seconds = 5;
var percentage = 0;	

function barUpdate() {
	var style = document.getElementById("test").style.width;
   	setTimeout(function () {                              
    if (counter < seconds) { 
    	counter = counter + 0.1;   
      	percentage = counter/seconds*100;
      	document.getElementById("test").style.width=percentage+"%";
        console.log(counter);  
        myLoop();              
    }
    else {
      	console.log("DONE!");
     	}
   	}, 100) 
}

