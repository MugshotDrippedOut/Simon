alert("Ahoj");
document
  .querySelector(
    "#main > div.w3-row.w3-padding-32.ws-light-green > div > div.w3-col.l6.w3-center > a:nth-child(3)"
  )
  .click();

// get number of all anchors on the page
document.querySelectorAll("a").length;

// select body and change background color
document.querySelector("body").style.backgroundColor = "lightblue";


// select first div with class w3-col and change background color
document.querySelector(
  "#main > div.w3-row.w3-padding-32.ws-light-green > div > div.w3-col.l6.w3-center"
).style.backgroundColor = "lightblue";

// Open new window with w3schools
window.open("https://www.w3schools.com/", "blank");


// Set value of input with id search2 to "HTML" and click on first link in subtopnav
document.querySelector("#search2").value = "HTML"; 
document.querySelector("#subtopnav > a.ga-nav.subtopnav_firstitem").click()

// create new array with colors and change background color of first div with class w3-col every 2 seconds
let colors = ["red", "green", "blue", "yellow", "pink", "purple"];
let i = 0;
setInterval(() => {
  document.querySelector(
    "#main > div.w3-row.w3-padding-32.ws-light-green > div > div.w3-col.l6.w3-center"
  ).style.backgroundColor = colors[i];
  i = (i + 1) % colors.length;
}, 2000);

// make every anchor hidden when hover
document.querySelectorAll("a").forEach((a) => {
  a.addEventListener("mouseover", (e) => {
    e.target.style.display = "none";
  });
});