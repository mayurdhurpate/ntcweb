$(document).ready(function(){
	$("#register_form").submit(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: '/smchallenge/register-submit/',
            data: $("#register_form").serialize(),
            success: function(data){
                if(data.result==true){
                    console.log("User Registered. Proceeding to Login!");
                    window.location.replace("/smchallenge/login/");
                }

                console.log(data);
            }
        });
	});

});