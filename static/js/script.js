function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function myFunction2() {
  var x = document.getElementById("myInput2");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}


function learnMore() {
  document.getElementById('learn-more-div').style.height = '100%'
   document.getElementById('learn-more').style.display = 'none'
   document.getElementById('dont-learn-more').style.display = 'block'
}

function dontLearnMore() {
  document.getElementById('learn-more-div').style.height = '100px'
   document.getElementById('learn-more').style.display = 'block'
   document.getElementById('dont-learn-more').style.display = 'none'
}