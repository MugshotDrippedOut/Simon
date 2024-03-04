window.onload = function () {
  var h1Height = window
    .getComputedStyle(document.querySelector("h1"))
    .getPropertyValue("height");
  var img = document.querySelector("#first img");
  img.style.maxHeight = parseInt(h1Height) * 3 + "px";
};

var themes = [
  {
    "--nav-footer": "#847106",
    "--bg-primary": "#eed45d",
    "--bg-secondary": "#fcfee8",
    "--nav-footer-text": "#ffffff",
  },
  {
    "--nav-footer": "#106784",
    "--bg-primary": "#5deed4",
    "--bg-secondary": "#e8fcfe",
    "--nav-footer-text": "#ffffff",
  },
  {
    "--nav-footer": "#781061",
    "--bg-primary": "#d45dee",
    "--bg-secondary": "#fee8fc",
    "--nav-footer-text": "#ffffff",
  },
];
var currentTheme = 0;
let themeButton = document.getElementById("theme");
themeButton.addEventListener("click", function () {
  currentTheme = (currentTheme + 1) % themes.length;
  for (let key in themes[currentTheme]) {
    document.documentElement.style.setProperty(key, themes[currentTheme][key]);
  }
});
