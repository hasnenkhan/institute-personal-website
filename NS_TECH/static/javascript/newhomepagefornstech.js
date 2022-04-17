var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

//enquiryform
function enquiryForm() {
  document.getElementById("myForm").style.display = "block";
} 
function closeForm() {
  document.getElementById("myForm").style.display = "None";
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

//dropdown

function showdd() {
  document.getElementById("altdd").style.display = "block";
}
window.addEventListener('mouseup',function(event){
  var box = document.getElementById('altdd');
  if(event.target != box  && event.target.parentNode != box) {
    box.style.display = 'none';
  }
});
