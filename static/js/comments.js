// for modal
// $('#myModal').on('shown.bs.modal', function () {
//   $('#myInput').trigger('focus')
// })
$(document).ready(function(){
  $("#myBtn").click(function(){
      $("#myModal").modal({remote: 'comments.html'});
      
  });
});
// function openModal() {
//   htmx.on("htmx:afterSwap", (e) => {
//       if (e.detail.target.id == "dialog") {
//           let modal = document.querySelector(".modal");
//           modal.style.animation = "appear 0.2s ease-out forwards";
//       }
//   })
// }

// function closeModal() {
//   let modal = document.querySelector(".modal");
//   modal.style.display = "none"
// }