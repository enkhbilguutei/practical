const square = document.getElementById("square");
const clickMe = document.getElementById("clickMe");

function doDemo() {
  const button = this;
  square.style.backgroundColor = "#00000";
  button.setAttribute("disabled", "true");
  setTimeout(clearDemo, 2000, button);
}

function clearDemo(button) {
  square.style.backgroundColor = "transparent";
  button.removeAttribute("disabled");
}

clickMe.onclick = doDemo;

// var square = document.getElementById("square");
// clickMe = document.getElementById("clickMe");
// function doDemo() {
//   var button = this;
//   square.style.backgroundColor = "#fa4";
//   button.setAttribute("disbaled", "true");
//   setTimeout(clearDemo, 2000, button);
// }

// function clearDemo(button) {
//   var square = document.getElementById("square");
//   square.style.backgroundColor = "transparent";
//   button.removeAttribute("disabled");
// }
// clickMe.onclick = doDemo;
