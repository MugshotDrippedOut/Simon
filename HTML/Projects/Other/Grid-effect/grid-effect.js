// variables
let columns = 0,
  rows = 0;

let count = -1;

// const
const wrapper = document.getElementById("tiles");

const colors = [
  "#FF0000",
  "#FF7F00",
  "#FFFF00",
  "#00FF00",
  "#0000FF",
  "#4B0082",
  "#8F00FF",
];

const handleOnClick = (index) => {
  count = count + 1;

  // anime.js for animation
  anime({
    targets: ".tile",
    backgroundColor: colors[(count % colors.length) - 1],
    delay: anime.stagger(50, { grid: [columns, rows], from: index }), // increase delay by 50ms for each elements.
  });
};

// create tile
const createTile = (index) => {
  const tile = document.createElement("div");

  tile.classList.add("tile");
  tile.onclick = (e) => handleOnClick(index);
  return tile;
};

// create tiles
const createTiles = (quantity) => {
  Array.from(Array(quantity)).map((tile, index) => {
    wrapper.appendChild(createTile(index));
  });
};

// create grid
const createGrrid = () => {
  wrapper.innerHTML = "";

  columns = Math.floor(document.body.clientWidth / 50);
  rows = Math.floor(document.body.clientHeight / 50);

  wrapper.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;
  wrapper.style.gridTemplateRows = `repeat(${rows}, 1fr)`;

  createTiles(columns * rows);
};

createGrrid();

window.onresize = () => createGrrid();
