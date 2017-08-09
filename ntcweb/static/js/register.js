$(document).ready(function(){
	$("#register_form").submit(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: '/smchallenge/register-submit/',
            data: $("#register_form").serialize(),
            success: function(data){
                if(data.result==true)
                    alert("User Registered. Proceed to Login!")
                console.log(data);
            }
        });
	});

});