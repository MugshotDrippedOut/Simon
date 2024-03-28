let btn = document.querySelector("button");
let body = document.querySelector("body");

let clicks = document.querySelector("#clicks");

let counter = 0;

const handleOnClick = () => {
  // move the button
  btn.style.left = Math.random() * 80 + "vw";
  btn.style.top = Math.random() * 80 + "vh";
  // change the color
  btn.style.backgroundColor =
    "rgb(" +
    Math.random() * 255 +
    "," +
    Math.random() * 255 +
    "," +
    Math.random() * 255 +
    ")";

  counter++;
  clicks.textContent = counter;
  switch (true) {
    case counter % 50 === 0:
      body.style.backgroundColor =
        "rgb(" +
        Math.random() * 255 +
        "," +
        Math.random() * 255 +
        "," +
        Math.random() * 255 +
        ")";
      break;
    case counter % 5 === 0:
      btn.style.color =
        "rgb(" +
        Math.random() * 255 +
        "," +
        Math.random() * 255 +
        "," +
        Math.random() * 255 +
        ")";
      break;
      case counter % 10 === 0:
        btn.style.fontSize = Math.random() * 50 + "px";
    default:
      break;
  }
};

btn.addEventListener("click", handleOnClick);

var cisli1 = "5";

var cisli2 = 6;

console.log(cisli1 * 1 + cisli2);

let text1 = "text";

let text2 = "text";
