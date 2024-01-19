// Constants
const gridContainer = document.getElementById("grid-container");

// Variables
let gridSize = 24;
let itemColor = "black";

// Create grid
function createGrid(size) {
  for (let i = 0; i < size * size; i++) {
    const gridItem = document.createElement("div");
    gridItem.classList.add("grid-item");
    gridContainer.appendChild(gridItem);
  }
  gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
  gridContainer.style.gridTemplateRows = `repeat(${size}, 1fr)`;
}

// Change color of grid item
function changeColor(e) {
  e.target.style.backgroundColor = itemColor;
}

// Clear grid
function clearGrid() {
  while (gridContainer.firstChild) {
    gridContainer.removeChild(gridContainer.firstChild);
  }
}

// Cycle through colors
function cycleColors() {
  const colors = ["black", "red", "orange", "yellow", "green", "blue", "purple"];
  let colorIndex = colors.indexOf(itemColor);
  if (colorIndex === colors.length - 1) {
    colorIndex = 0;
  } else {
    colorIndex++;
}
itemColor = colors[colorIndex];
}

// Add event listener to grid items
gridContainer.addEventListener("mouseover", changeColor);
gridContainer.addEventListener("click", cycleColors);
createGrid(gridSize);
