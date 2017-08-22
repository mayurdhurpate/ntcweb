$(document).ready(function(){
	$("#coordinator_form").submit(function(event){
        event.preventDefault();
        var $form = $( this );
        $.ajax({
            type: "POST",
            url: $form.attr("action"),
            data: $("#coordinator_form").serialize(),
            success: function(data){
                if(data.result==true){
                    console.log("College Submitted");
                }

                console.log(data);
            }
        });
	});

});