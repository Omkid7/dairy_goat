$(document).ready(function(){
  $(function () {

    $("#plist").DataTable({
      "responsive": true, "lengthChange": true, "autoWidth": false,
      "buttons": ["excel","print"],
      "lengthMenu": [10]
    }).buttons().container().appendTo('#plist_wrapper .col-md-6:eq(0)');
    // $('#plist').DataTable({
    //   "lengthChange": true,
     
    //   "lengthMenu":[5]
    // });
  
  });

  setTimeout(function() {
    $('.alert').fadeOut('fast');
  }, 2000); 
  $("#id_dog_id").select2({
    placeholder: "Dispense dog Here",
    allowClear: true
});



  

$("#id_dog_id").select2();
$("#id_dog_id").on("select2:open", function (e) {
  
  $('#id_dog_id').change(function(){
        var data= $(this).val();
        // alert(data);       
        $("#id_taken").val(data)
         
      });

     $('#select2-search__field')
         .text(dogname)
         .trigger('change');
});
  // $('.dataTable').paging({limit:6});




  
  $('.theme-loader').fadeOut(500);
  $('#id_dog_id').select2({
    placeholder:" Search Deployed Dog here",
    width:"100%",



 })


 
    
$(function() {
  $("#filter2").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#plist  > tr").filter(function() {      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});



})

  // $(function(){
    //     $('#id_dog_id').change(function(){
    //     var data= $(this).val();
    //     alert(data);       
    //     $("#id_sto").val(data)
         
    //   });
     
    //  $('#select2-search__field')
    //      .text(dogname)
    //      .trigger('change');
    
    //   });


    // $("#select2-search__field").on("click", function() {

    //   $('#id_dog_id').change(function(){
    //         var data= $(this).val();
    //         alert(data);       
    //         $("#id_sto").val(data)
             
    //       });
         
    //      $('#select2-search__field')
    //          .text(dogname)
    //          .trigger('change');
    
    //     });