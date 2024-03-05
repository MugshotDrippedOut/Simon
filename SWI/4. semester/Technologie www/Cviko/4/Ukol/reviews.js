/*
<div class="review" data-index="0">
    <img src="Images/roblox5.jpg" alt="profile_pisctre" />
    <div>
    <h3>John Doe</h3>
    <p>
        This game is amazing! I love it! I play it every day and I can't get enough of it!
    </p>
    <div class="stars">
        <div class="stars">
        <i class="fas fa-star active" ></i>
        <i class="fas fa-star active"></i>
        <i class="fas fa-star active"></i>
        <i class="fas fa-star active"></i>
        <i class="fas fa-star"></i>
        </div>
    </div>
    </div>
</div>
*/
const randomFromArray = (array) => {
  return array[Math.floor(Math.random() * array.length)];
};

let images = [
  "Images/roblox1.jpg",
  "Images/roblox2.jpg",
  "Images/roblox3.jpg",
  "Images/roblox4.jpg",
  "Images/roblox5.jpg",
  "Images/roblox6.jpg",
  "Images/roblox7.jpg",
];

let profiles = [
  { name: "John Doe", profilePicture: randomFromArray(images) },
  { name: "Jane Doe", profilePicture: randomFromArray(images) },
  { name: "John Smith", profilePicture: randomFromArray(images) },
  { name: "Jane Smith", profilePicture: randomFromArray(images) },
  { name: "Alice Johnson", profilePicture: randomFromArray(images) },
  { name: "Bob Anderson", profilePicture: randomFromArray(images) },
  { name: "Eva Wilson", profilePicture: randomFromArray(images) },
  { name: "David Miller", profilePicture: randomFromArray(images) },
  { name: "Linda Davis", profilePicture: randomFromArray(images) },
  { name: "Tom Harris", profilePicture: randomFromArray(images) },
  { name: "Emily White", profilePicture: randomFromArray(images) },
  { name: "Michael Lee", profilePicture: randomFromArray(images) },
  { name: "Olivia Martinez", profilePicture: randomFromArray(images) },
  { name: "William Turner", profilePicture: randomFromArray(images) },
  { name: "Sophia Rodriguez", profilePicture: randomFromArray(images) },
  { name: "Daniel Thompson", profilePicture: randomFromArray(images) },
  { name: "Emma Baker", profilePicture: randomFromArray(images) },
  { name: "Christopher Harris", profilePicture: randomFromArray(images) },
  { name: "Ava Mitchell", profilePicture: randomFromArray(images) },
  { name: "Matthew Clark", profilePicture: randomFromArray(images) },
  { name: "Mia Adams", profilePicture: randomFromArray(images) },
  { name: "Joseph Hall", profilePicture: randomFromArray(images) },
  { name: "Ella Turner", profilePicture: randomFromArray(images) },
  { name: "Andrew Scott", profilePicture: randomFromArray(images) },
  { name: "Grace Lewis", profilePicture: randomFromArray(images) },
  { name: "Christopher Evans", profilePicture: randomFromArray(images) },
  { name: "Sophia Hill", profilePicture: randomFromArray(images) },
  { name: "Jack Wright", profilePicture: randomFromArray(images) },
  { name: "Lily Collins", profilePicture: randomFromArray(images) },
  { name: "Ryan Cooper", profilePicture: randomFromArray(images) },
  { name: "Avery Murphy", profilePicture: randomFromArray(images) },
  { name: "Lucas Turner", profilePicture: randomFromArray(images) },
  { name: "Madison Bennett", profilePicture: randomFromArray(images) },
  { name: "Carter Parker", profilePicture: randomFromArray(images) },
  { name: "Victoria Brooks", profilePicture: randomFromArray(images) },
  { name: "Henry Ward", profilePicture: randomFromArray(images) },
  { name: "Aria Allen", profilePicture: randomFromArray(images) },
  { name: "Nathan Hayes", profilePicture: randomFromArray(images) },
  { name: "Aubrey Simmons", profilePicture: randomFromArray(images) },
];

let reviews = [
  {
    profile: randomFromArray(profiles),
    review:
      "This game is amazing! I love it! I play it every day and I can't get enough of it!",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is the best! I play it every day and I can't get enough of it!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is amazing! I love it! I play it every day and I can't get enough of it!",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is the best! I play it every day and I can't get enough of it!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is so hilarious! I can't stop laughing at the quirky characters and absurd situations. Definitely a 5-star comedy show!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Worst game ever! I'd rather watch paint dry. The graphics are terrible, the controls are a nightmare, and the storyline is as interesting as a blank sheet of paper. 1 star, and that's being generous.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I thought this was a game, but it's actually a masterpiece of modern art. I don't understand a thing, and that's the beauty of it. 5 stars for avant-garde confusion!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I play this game just to annoy my neighbors with the annoying soundtrack. It's a perfect tool for revenge. 1 star for being an effective annoyance.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "The graphics are so pixelated; I thought I accidentally stumbled into a time machine and landed in the '90s. 2 stars for the unintended nostalgia trip.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I named my pet rock after this game because they both have the same level of excitement. 1 star for making me appreciate my pet rock more.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like a bad joke - you keep waiting for the punchline, but it never comes. 1 star for the disappointment.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I accidentally bought this game thinking it was something else. Now, I'm stuck with it. 1 star for my lack of attention to detail.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like a pizza with pineapple - it may have its fans, but for the rest of us, it's just wrong. 2 stars for the attempt at uniqueness.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game and lost 10 IQ points. Now I can join the 'Dumb and Dumber' fan club. 1 star for making me feel intellectually challenged.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I thought this was a horror game, but it turned out to be the scariest thing I've ever experienced - a complete waste of time. 1 star for the unexpected fright.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game on a potato, and it made the potato feel bad about its performance. 1 star for hurting my potato's feelings.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I've seen better graphics on my grandma's knitting. 1 star for making me appreciate my grandma's craftsmanship.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is so bad, it makes 'The Room' look like a cinematic masterpiece. 1 star for achieving a new level of awfulness.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game and now believe in aliens. Clearly, extraterrestrials made this abomination. 1 star for convincing me of the existence of ET game developers.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Absolutely mind-blowing! This game made me question the meaning of life. 6 out of 5 stars!",
    stars: 6,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Worst game ever! I'd rather watch paint dry. Uninstalling immediately.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is a masterpiece, but only if you're into watching grass grow. 2 stars for the thrilling lawn mowing simulation.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Hilarious! I spent more time laughing at the bugs than playing the actual game. 3 stars for the unintentional comedy.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I'm convinced the developers let a monkey design the levels. It's chaos. 1 star for effort, though.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Best game ever! Just kidding. It's as enjoyable as stepping on a LEGO. 1 star for painful memories.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "If you enjoy frustration and disappointment, this game is for you. Negative stars if possible!",
    stars: 0,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I've seen better graphics on my grandma's flip phone. Is this a game or a time machine to the '90s?",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Not bad, but the in-game currency is so scarce, I had to take out a mortgage to buy a virtual sandwich. 2 stars for financial ruin.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this for 10 minutes and felt my IQ dropping. It's like a black hole for intelligence. 1 star for science.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game cured my insomnia. The monotony is a powerful sleep aid. 3 stars for its unintentional medicinal qualities.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Trollolol! This game is a masterpiece... of disaster. It's so bad it's good. 5 stars for trolling potential.",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I spent more time watching loading screens than playing. It's like a game within a loading screen simulator. 1 star for inception.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Absolutely dreadful. I wouldn't recommend this game to my worst enemy. -5 stars if possible.",
    stars: -5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Is this a game or a social experiment? I feel like I'm being punked. 2 stars for the psychological thriller experience.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I accidentally clicked the 'buy' button and now I want a refund for my wasted time. 1 star for buyer's remorse.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is amazing! I love it! I play it every day and I can't get enough of it!",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is the best! I play it every day and I can't get enough of it!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is fantastic! The graphics are stunning, and the gameplay is addictive. I recommend it to everyone!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I've been playing this game for weeks, and it never gets old. The storyline is captivating, and the characters are well-developed. Definitely a 5-star game!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I'm impressed by the attention to detail in this game. The developers have done an excellent job. I can't stop playing!",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "The multiplayer experience in this game is unparalleled. I've made friends from around the world while playing. Kudos to the developers!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game exceeded my expectations. The challenges are well-balanced, and the rewards are satisfying. A solid 4-star rating from me!",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Absolutely dreadful! I can't believe I wasted my time on this game. The controls are terrible, and the graphics are a joke. 1 star, and that's being generous.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Who created this mess? It's like playing a game from the '90s. Do yourself a favor and avoid it at all costs. 1 star because I can't give it zero.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Hilarious! This game is so bad it's good. I can't stop laughing at the ridiculousness. 5 stars for the unintentional comedy.",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I thought I accidentally stumbled into a time machine and ended up in the past. The graphics are ancient, and the gameplay is worse. 2 stars for nostalgia, I guess.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is a masterpiece! The glitches and bugs make it even more enjoyable. It's like a secret feature. 5 stars for the unpredictable experience.",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I'm not sure if the developers were high when they made this, but it's a wild ride. The randomness is both frustrating and entertaining. 3 stars for the confusion.",
    stars: 3,
  },
];

let reviewsIndex = 0;
console.log(reviews);

for (let i = 0; i < reviews.length; i++) {
  let review = reviews[i];
  let div = document.createElement("div");
  div.classList.add("review");
  div.dataset.index = i;
  let img = document.createElement("img");
  img.src = review.profile.profilePicture;
  img.alt = "profile_picture";
  div.appendChild(img);
  let div2 = document.createElement("div");
  div.appendChild(div2);
  let h3 = document.createElement("h3");
  h3.innerText = review.profile.name;
  div2.appendChild(h3);
  let p = document.createElement("p");
  p.innerText = review.review;
  div2.appendChild(p);
  let div3 = document.createElement("div");
  div3.classList.add("stars");
  div2.appendChild(div3);
  for (let j = 0; j < 5; j++) {
    let i = document.createElement("i");
    i.classList.add("fas");
    i.classList.add("fa-star");
    if (j < review.stars) {
      i.classList.add("active");
    }
    div3.appendChild(i);
  }
  document.getElementById("reviews").appendChild(div);
}
