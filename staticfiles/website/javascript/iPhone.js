
document.addEventListener("DOMContentLoaded", function() {
  if (window.innerWidth < 900) {
    document.getElementById("iPhone").classList.remove("w-50");
  } else {
    document.getElementById("iPhone").classList.remove("w-100");
  }
});


document.addEventListener("DOMContentLoaded", function(event) {
  var element = document.querySelector('.iPhone');

  function resize() {
    if (window.innerWidth < 900) {
      element.classList.remove('w-50');
    } else {
      element.classList.remove('w-100');
    }
  }
  // For performance reasons, this method should be
  // "debounced" so that it doesn't have to execute
  // on every resize event, only when you're done resizing.
  window.onresize = resize;
});
