"use strict";
const ContainerEl = document.querySelector(".container");
let playerTxt = document.querySelector(".message");
let restartBtn = document.querySelector("restartbtn");
let boxes = document.querySelectorAll(".box");

const O_TXT = "O";
const X_TXT = "X";

let currentPlayer = O_TXT;
let spaces = Array(9).fill(null);

let winnerIndicator = getComputedStyle(document.body).getPropertyValue(
  "--darkColor"
);

//start game

const startGame = () => {
  boxes.forEach((boxs) => boxs.addEventListener("click", boxClicked));
};

// box clicked

function boxClicked(e) {
  const id = e.target.id;

  // check id
  if (!spaces[id]) {
    spaces[id] = currentPlayer;
    e.target.innerText = currentPlayer;

    // winner logic
    if (playerHasWon() != false) {
      playerTxt.innerHTML = `<h2 class="message">Congratulation Player ${currentPlayer} </h2>`;
      winnerIndicator = playerHasWon();

      winnerIndicator.map(
        (box) => (boxes[box].style.backgroundColor = "#f4d03f")
      );

      ContainerEl.classList.add("success");
    }
    // draw logic
    else if (!spaces.includes(null)) {
      playerTxt.innerHTML = `<h2 class="message">Draw</h2>`;
      ContainerEl.classList.add("success");
      document.getElementById("myParagraph").style.display = "none";
    }
    currentPlayer = currentPlayer === X_TXT ? O_TXT : X_TXT;
  }
}

// wining combination
const winingCombination = [
  [0, 1, 2], // top row
  [3, 4, 5], // mid row
  [6, 7, 8], // bottom row
  [0, 3, 6], // left col
  [1, 4, 7], // mid col
  [2, 5, 8], // right col
  [0, 4, 8], // left diagonal
  [2, 4, 6], // right diagonal
];

// player win
function playerHasWon() {
  for (const condition of winingCombination) {
    let [a, b, c] = condition;

    if (spaces[a] && spaces[a] === spaces[b] && spaces[a] === spaces[c]) {
      return [a, b, c];
    }
  }
  return false;
}

// restart game

restartbtn.addEventListener("click", restartGame);

function restartGame() {
  spaces.fill(null);

  boxes.forEach((box) => {
    box.innerHTML = "";
    box.style.backgroundColor = "";
  });

  playerTxt.innerHTML = "Tic Tac Toe";
  currentPlayer = O_TXT;
  ContainerEl.classList.remove("success");
  document.getElementById("myParagraph").style.display = "block";
}

startGame();
