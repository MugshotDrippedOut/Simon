let imageUrls = [
  "https://wallpapers.com/images/high/funny-roblox-pictures-7et2vu9scjlutvxl.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-cl6pkpdgr8kwoadr.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-cqwuiszv4zir2bnk.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-kieik74uww0c1i91.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-63y44wpkp9jg7cje.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-6vvcg0pcmu5sml2q.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-34odehkaimc66ypy.webp",
  "https://wallpapers.com/images/high/zoomed-in-roblox-pfp-540xh5q6p2yf2wej.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-rdqbswr0bpx8sbko.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-td2pbvlf3vgkees4.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-oera6y4qya1s1zp5.webp",
  "https://wallpapers.com/images/high/funny-roblox-pictures-v4ues984cq0weoyo.webp",
  "https://tr.rbxcdn.com/136d435bd592678def1913e5078aee22/420/420/Hat/Png",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBk1mSywWS3rOvlkAz9qNU7S6E3exDIsLQkg&usqp=CAU",
  "https://www.publicdomainpictures.net/pictures/210000/nahled/funny-guy-1488320380Lm4.jpg",
  "https://i.kym-cdn.com/photos/images/newsfeed/002/461/188/20d.png",
  "https://e0.pxfuel.com/wallpapers/591/302/desktop-wallpaper-stewie-family-guy-face-griffin-roblox-stewiegriffin-111222333444555-man-funny.jpg",
  "https://tr.rbxcdn.com/74ebc1e38c9356e8b728325cb86334af/420/420/Hat/Png",
  "data:image/jpeg;base64,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",
  "https://i.pinimg.com/236x/e9/4a/31/e94a31606e4b9cd577c10586778b2ba0.jpg",
  "https://i.redd.it/3g9u1ml7wme71.jpg",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPJIZOanBeCY02ZhSdZ_kfTDCksh6LUsw3ug&usqp=CAU",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLrLUX-S73uTuyalO2-T-wIu78L_4EUpIMew&usqp=CAU",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjxiO72V696EH7l6i9-R-jxgkh3Pxzw-lBGQ&usqp=CAU",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGI6Mf0-R9Ru1nxmA1LfBdYXLtkXJV48Cxqw&usqp=CAU",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQK1wfCuUFQqsxCVMY2Wp4LFLfTQdZl4TVrJQ&usqp=CAU",
];

let imageIndex = 0;
let activeIndex = 0;

const groups = document.getElementsByClassName("card-group");

var allGroups = document.getElementsByClassName("card-groups");

/* 
this is the total number of cards, including the ones that are not visible,
reduce is a function that takes an array and a function, the function is called for each element of the array, 
the first argument is the accumulator, the second is the current element, the function returns the new value of the accumulator, 
the second argument of reduce is the initial value of the accumulator 
*/
var totalCards = Array.from(groups).reduce(
  (total, group) => total + group.children.length,
  0
);

while (imageUrls.length > totalCards) {
  console.log("Adding new cards");
  var newGroup = document.createElement("div");
  newGroup.classList.add("card-group");
  newGroup.dataset.index = groups.length;
  if (groups.length == 0) { // the first group is active
    newGroup.dataset.status = "active";
  } else {
    newGroup.dataset.status = "unknown";
  }
  for (let i = 0; i < 8; i++) { // 8 cards per group
    var card = document.createElement("div");
    if (i % 2 == 0) {
      card.classList.add("little-card", "card");
    } else {
      card.classList.add("big-card", "card");
    }
    var img = document.createElement("img");
    img.src = imageUrls[imageIndex % imageUrls.length];
    img.alt = "Image";
    card.appendChild(img);
    newGroup.appendChild(card);
    imageIndex++;
  }
  allGroups[0].appendChild(newGroup); // append the new group to the first card-group
  totalCards += 8;
  console.log(totalCards);
  console.log(imageUrls.length);
}

const handleRightClick = () => {
  const nextIndex = activeIndex + 1 <= groups.length - 1 ? activeIndex + 1 : 0;
  const currentGroup = document.querySelector(
    "[data-index='" + activeIndex + "']"
  );
  const nextGroup = document.querySelector("[data-index='" + nextIndex + "']");

  currentGroup.dataset.status = "after";

  nextGroup.dataset.status = "becoming-active-from-before";

  setTimeout(() => {
    nextGroup.dataset.status = "active";
    activeIndex = nextIndex;
  }, 200);
};

const handleLeftClick = () => {
  const nextIndex = activeIndex - 1 >= 0 ? activeIndex - 1 : groups.length - 1;
  const currentGroup = document.querySelector(
    "[data-index='" + activeIndex + "']"
  );
  const nextGroup = document.querySelector("[data-index='" + nextIndex + "']");

  currentGroup.dataset.status = "before";

  nextGroup.dataset.status = "becoming-active-from-after";

  setTimeout(() => {
    nextGroup.dataset.status = "active";
    activeIndex = nextIndex;
  }, 200);
};

var cards = document.querySelectorAll(".card");

cards.forEach(function (card) {
  card.addEventListener("click", function () {
    cards.forEach(function (card) {
      card.classList.remove("active");
    });

    this.classList.add("active");
  });
});
