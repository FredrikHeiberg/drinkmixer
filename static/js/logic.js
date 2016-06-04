var drinkName = "";
var drinkSize = 0;
var drinkOrder = [];

$(document).ready(function() {
	$("#warning").hide();
	$('#romCoke').click(function() {
		drinkName = "romCoke";
		$('#drink-name').val(drinkName);
		$(this).animate({opacity:0.5}, 1000);
		$('#ginTonic').animate({opacity:1}, 1000);
		$('#vodkaFanta').animate({opacity:1}, 1000);
		check();
	})

	$('#ginTonic').click(function() {
		drinkName = "ginTonic";
		$('#drink-name').val(drinkName);
		$(this).animate({opacity:0.5}, 1000);
		$('#romCoke').animate({opacity:1}, 1000);
		$('#vodkaFanta').animate({opacity:1}, 1000);
		check();
	})

	$('#vodkaFanta').click(function() {
		drinkName = "vodkaFanta";
		$('#drink-name').val(drinkName);
		$(this).animate({opacity:0.5}, 1000);
		$('#romCoke').animate({opacity:1}, 1000);
		$('#ginTonic').animate({opacity:1}, 1000);
		check();
	})

	$('#40').click(function() {
		drinkSize = 40;
		$("#drink-size").val(drinkSize);
		check();
	})

	$('#200').click(function() {
		drinkSize = 200;
		$("#drink-size").val(drinkSize);
		check();
	})

	$('#400').click(function() {
		drinkSize = 400;
		$("#drink-size").val(drinkSize);
		check();
	})

	// $('#mix').click(function() {
	// 	drinkOrder = [drinkName, drinkSize];
	// 	$('#ginTonic').animate({opacity:1}, 1000);
	// 	$('#romCoke').animate({opacity:1}, 1000);
	// 	$('#vodkaFanta').animate({opacity:1}, 1000);
	// 	console.log("WTF! " + drinkSize + " " + drinkName)


	// 	var data = {
	// 		name: drinkName,
	// 		size: drinkSize
	// 	};

	// 	$.ajax({
	// 		type: 'POST',
	// 		url: '/process',
	// 		data: JSON.stringify(data),
	// 		dataType: 'json',
	// 		contentType: 'application/json; charset=utf-8'
	// 	}).done(function(msg) {
	// 		alert("Data Saved: " + msg);
	// 	});


	// 	drinkSize = 0;
	// 	drinkName = "";
	// 	console.log(drinkName);
	// })
});

function check() {
	if (drinkSize != 0 && drinkName != "") {
		$('#mix').removeAttr('disabled');
	}
}