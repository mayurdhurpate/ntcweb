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
                    $("#id_talk").prop("checked", false);
                    $("#id_talk").prop("disabled", false);
                    $("#id_venue").prop("checked", false);
                    $("#id_venue").prop("disabled", false);
                    $("#id_course_id").prop("disabled", true);
                    $("#coordinator_form")[0].reset();
                    alert("College Submitted for approval for Teacher: "+ data.teacher_code+"\nSubmit another college for your teacher code by filling above details again.");
                }

                console.log(data);
            }
        });
	});
    $('input[type=text], textarea').addClass("form-control");
    $('textarea').attr('rows','1');
    $("label[for='id_course']").before("<br><h3>Art of Living Campus Activities</h3><br>");
    $("#id_course_id").prop("disabled", true);
    $('#id_course').change(function() {
        // this will contain a reference to the checkbox   
        if (this.checked) {
            // the checkbox is now checked 
            $("#id_talk").prop("checked", true);
            $("#id_talk").prop("disabled", true);
            $("#id_venue").prop("checked", true);
            $("#id_venue").prop("disabled", true);
            $("#id_course_id").prop("disabled", false);
        } else {
            // the checkbox is now no longer checked
            $("#id_talk").prop("checked", false);
            $("#id_talk").prop("disabled", false);
            $("#id_venue").prop("checked", false);
            $("#id_venue").prop("disabled", false);
            $("#id_course_id").prop("disabled", true);
        }
    });

});