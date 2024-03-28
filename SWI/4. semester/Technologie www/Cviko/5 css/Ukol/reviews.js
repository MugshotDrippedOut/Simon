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
  { name: "Al Beback", profilePicture: randomFromArray(images) },
  { name: "Sue Mee", profilePicture: randomFromArray(images) },
  { name: "Ben Dover", profilePicture: randomFromArray(images) },
  { name: "Anita Bath", profilePicture: randomFromArray(images) },
  { name: "Barb Dwyer", profilePicture: randomFromArray(images) },
  { name: "Eileen Dover", profilePicture: randomFromArray(images) },
  { name: "Gail Forcewind", profilePicture: randomFromArray(images) },
  { name: "Hal Jalikee", profilePicture: randomFromArray(images) },
  { name: "Ivana Tinkle", profilePicture: randomFromArray(images) },
  { name: "Justin Time", profilePicture: randomFromArray(images) },
  { name: "Maya Normousbutt", profilePicture: randomFromArray(images) },
  { name: "Neil Down", profilePicture: randomFromArray(images) },
  { name: "Olive Yew", profilePicture: randomFromArray(images) },
  { name: "Paige Turner", profilePicture: randomFromArray(images) },
  { name: "Seymour Butz", profilePicture: randomFromArray(images) },
  { name: "Drew Peacock", profilePicture: randomFromArray(images) },
  { name: "Iona Ford", profilePicture: randomFromArray(images) },
  { name: "Chris P. Bacon", profilePicture: randomFromArray(images) },
  { name: "Al O'Moaney", profilePicture: randomFromArray(images) },
  { name: "Hugh Jass", profilePicture: randomFromArray(images) },
  { name: "Eva Destruction", profilePicture: randomFromArray(images) },
  { name: "Izzy Backyet", profilePicture: randomFromArray(images) },
  { name: "Warren Peace", profilePicture: randomFromArray(images) },
  { name: "Art Major", profilePicture: randomFromArray(images) },
  { name: "Anita Bathwater", profilePicture: randomFromArray(images) },
  { name: "Chris Cross", profilePicture: randomFromArray(images) },
  { name: "Al Kaseltzer", profilePicture: randomFromArray(images) },
  { name: "Barb Dwyer", profilePicture: randomFromArray(images) },
  { name: "Sofa King", profilePicture: randomFromArray(images) },
  { name: "Kandi Barr", profilePicture: randomFromArray(images) },
  { name: "Robin Banks", profilePicture: randomFromArray(images) },
  { name: "Will Power", profilePicture: randomFromArray(images) },
  { name: "Justin Case", profilePicture: randomFromArray(images) },
  { name: "Moe Lester", profilePicture: randomFromArray(images) },
  { name: "Nadia Seymour", profilePicture: randomFromArray(images) },
  { name: "Sandy Beech", profilePicture: randomFromArray(images) },
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
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like a rollercoaster of emotions. One minute, I'm having a blast, and the next, I'm questioning all my life choices. 4 stars for the emotional turmoil.",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game expecting a challenge, but it's so easy, even my pet rock could beat it. 2 stars for pet-friendly gameplay.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "My cat walked across the keyboard and accidentally gave this game a better rating than it deserves. 3 stars for feline input.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is a journey into the unknown, and by unknown, I mean the bizarre and inexplicable. 3 stars for the surreal experience.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game while eating cereal, and now every time I see a spoon, I get flashbacks. 2 stars for unexpected associations.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "If this game were a movie, it would be a low-budget indie film with a confusing plot and questionable acting. 2 stars for indie charm.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I accidentally became the leader of a virtual cult in this game. Now, I'm questioning my life choices. 3 stars for unintentional cult simulator.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like trying to juggle with one hand tied behind your back - frustrating and ultimately pointless. 1 star for the juggling attempt.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game during a power outage, and now I believe it's powered by dark magic. 2 stars for the mystical experience.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I tried to speedrun this game, but it's so slow, even a snail could beat my record. 1 star for the unintentional anti-speedrun feature.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I named my firstborn after the main character in this game. Now, I'm questioning my parenting decisions. 3 stars for the unexpected influence.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like a box of chocolates - you never know what you're gonna get, but you're pretty sure it won't be good. 2 stars for the Forrest Gump vibes.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game while multitasking, and now I'm convinced it's impossible to do anything else while playing. 1 star for monopolizing my attention.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I used this game to settle arguments with my friends. Whoever loses has to play it. 4 stars for its unintended dispute resolution capabilities.",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is so confusing; I had to create a mind map to navigate through the chaos. 3 stars for the unintentional brain exercise.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game and discovered the meaning of life. Just kidding, I'm still clueless. 1 star for the existential crisis.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game with my grandma, and she beat me every time. Now, she thinks she's a gaming prodigy. 3 stars for unintentional family bonding.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game in a dark room, and now I'm convinced it's haunted. 2 stars for the spooky atmosphere.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game during a boring meeting, and suddenly the meeting seemed like the highlight of my day. 1 star for making meetings seem exciting.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like a soap opera - full of drama, questionable plot twists, and overacting characters. 2 stars for the melodramatic experience.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game with my cat, and now he won't stop meowing at the screen. 3 stars for unexpected feline entertainment.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game with my grandma, and she thought it was a cooking simulator. Now, she wants to open a virtual bakery. 4 stars for inspiring culinary dreams.",
    stars: 4,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like trying to solve a Rubik's Cube blindfolded - frustrating and ultimately futile. 1 star for the puzzle challenge.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game and accidentally discovered the meaning of life. Just kidding, I'm still clueless. 1 star for the existential crisis.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game while eating pizza, and now every time I see pizza, I crave a better game. 2 stars for pizza-induced disappointment.",
    stars: 2,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This game is like trying to find a needle in a haystack, except the needle is the fun and the haystack is the game. 1 star for the challenging search.",
    stars: 1,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I played this game and now believe in parallel universes. In one of them, this game is actually good. 3 stars for the alternate reality experience.",
    stars: 3,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a masterpiece! The creativity and variety of experiences are mind-blowing. I can't get enough of the endless possibilities!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I've been playing this Roblox game for months, and it keeps getting better. The community is fantastic, and the developers are always adding exciting new features.",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "As a Roblox enthusiast, I can confidently say that this game is top-tier. The attention to detail and the constant updates make it a joy to play. Solid 5 stars!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a gem! The graphics are charming, the gameplay is engaging, and the community is welcoming. I recommend it to everyone!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Roblox never fails to amaze me, and this game is no exception. The immersive worlds and the ability to create your own adventures make it a 5-star experience.",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I'm addicted to this Roblox game! The variety of games within the platform is incredible. It's like having a gaming universe at your fingertips. 5 stars!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Roblox is the ultimate gaming platform, and this game showcases its true potential. From the graphics to the gameplay, everything is top-notch. 5-star excellence!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a testament to the creativity of the community. The possibilities are endless, and each playthrough feels like a unique adventure. 5 stars!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "If you're a Roblox enthusiast, this game is a must-play. The level of detail and the seamless integration of user-generated content make it a 5-star masterpiece.",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I've played countless Roblox games, but this one stands out. The developers have truly crafted something special. A solid 5 stars from a dedicated player!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a hidden gem. The community is friendly, the gameplay is addictive, and the constant updates keep things fresh. 5 stars without a doubt!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "As a long-time Roblox player, I can confidently say that this game is a highlight. The innovation and creativity on display make it a 5-star experience!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a masterpiece of game design. The controls are intuitive, the graphics are delightful, and the overall experience is nothing short of exceptional. 5 stars!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I can't get enough of this Roblox game! The community-driven content and the immersive gameplay make it a standout title. 5 stars for an outstanding gaming experience!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a playground of creativity. From building my own worlds to exploring others, the possibilities are endless. A solid 5-star rating!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Roblox has become a big part of my gaming life, and this particular game is a shining example of what makes the platform great. 5 stars for an amazing experience!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "I've played many Roblox games, and this one is a standout. The attention to detail, the engaging gameplay, and the friendly community make it a 5-star favorite!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game has it all - engaging gameplay, vibrant graphics, and a welcoming community. It's a 5-star experience that keeps me coming back for more!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "Roblox never ceases to amaze me, and this game is a prime example. The creativity, the variety, and the endless fun earn it a well-deserved 5-star rating!",
    stars: 5,
  },
  {
    profile: randomFromArray(profiles),
    review:
      "This Roblox game is a masterpiece that showcases the platform's potential. The community-driven content and the endless possibilities make it a 5-star favorite!",
    stars: 5,
  },

];

let reviewsIndex = 0;
let usedReviews = [];
console.log("All possible reviews");
console.log(reviews);

for (let i = 0; i < 8; i++) {
  let review = randomFromArray(reviews);
  while (usedReviews.includes(review)) {
    review = randomFromArray(reviews);
  }
  usedReviews.push(review);
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

console.log("Used reviews");
console.log(usedReviews);
