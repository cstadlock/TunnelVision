$(document).ready(function() {
        $('#dataTables-example').DataTable({
            responsive: true
        });
    });
    
    
function deleteOrder(form_id) {
    swal({
        title: "Are you sure?",
        text: "You will not be able to recover order",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, delete it!",
        closeOnConfirm: false
    }, function() {
         $(form_id).submit();
    });
}