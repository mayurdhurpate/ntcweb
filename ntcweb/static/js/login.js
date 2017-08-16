$(document).ready(function(){
	$("#register_form").submit(function(event){
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: '/smchallenge/login-submit/',
            data: $("#register_form").serialize(),
            success: function(data){
                if(data.result==true)
                    alert("User Logged in. Proceed to Dashboard!")
                console.log(data);
            }
        });
	});

});