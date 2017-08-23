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
                    $("#coordinator_form")[0].reset();
                    alert("College Submitted for approval for Teacher: "+ data.teacher_code+"\nSubmit another college for your teacher code by filling above details again.");
                }

                console.log(data);
            }
        });
	});

});