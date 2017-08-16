$(document).ready(function(){
	$("#submit_form").submit(function(event){
        var $form = $( this );
        
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $form.attr("action"),
            data: $("#submit_form").serialize(),
            success: function(data){
                if(data.result==true)
                    alert("Score Submitted. View changes in Leaderboard!")
                console.log(data);
            }
        });
	});
});