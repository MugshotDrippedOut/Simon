let trailers = [
  {
    name: "funny video",
    url: "https://www.youtube.com/embed/tSZZFayo64I",
    description: "funny video",
  },
  {
    name: "OMG",
    url: "https://www.youtube.com/embed/QemkUB8rHKQ",
    description: "funny video",
  },
  {
    name: "Aaa",
    url: "https://www.youtube.com/embed/t4BLFX4UC8o",
    description: "Vyľakalo ma to",
  },
  {
    name: "Whaaat",
    url: "https://www.youtube.com/embed/uapIh5SuvGc",
    description: "Unbelievable, my words can't describe it, you have to see it by yourself, it's amazing, it's incredible, it's...",
  },
  {
    name: "funny video",
    url: "https://www.youtube.com/embed/i7iX-deiYpQ",
    description: "funny video",
  },
  {
    name: "So sad",
    url: "https://www.youtube.com/embed/WjUvRs4pBuI",
    description: ":(",
  },
  {
    name: "So sadder",
    url: "https://www.youtube.com/embed/SMT6Q0NDVh8",
    description: ":,(",
  },
  {
    name: "WOOOOOOW",
    url: "https://www.youtube.com/embed/wjwqJi7ju2A",
    description: "HELL YEAH! W O W! ASHTONISHING! AMAZING! INCREDIBLE! UNBELIEVABLE",
  },
];

let trailerIndex = 0;
let activeIndex = 0;

console.log(trailers.length);

/*
<div class="trailer" data-index="0" data-status="active">
<label for="trailer1">a</label>
<iframe
    id="trailer1"
    width="560"
    height="315"
    src="https://www.youtube.com/embed/tSZZFayo64I"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
></iframe>
<div class="trailer-description">a</div>
</div>
*/
var trailerDiv = document.getElementById("trailers");
for (let i = 0; i < trailers.length; i++) {
  let trailer = trailers[i];
  let div = document.createElement("div");
  div.classList.add("trailer");
  div.dataset.index = i;
  if (i == 0) {
    div.dataset.status = "active";
  } else {
    div.dataset.status = "inactive";
  }
  let label = document.createElement("label");
  label.htmlFor = "trailer" + i; 
  label.innerText = trailer.name;
  div.appendChild(label);
  let iframe = document.createElement("iframe");
  iframe.id = "trailer" + i;
  iframe.width = "560";
  iframe.height = "315";
  iframe.src = trailer.url;
  iframe.frameborder = "0";
  iframe.allow =
    "accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
  iframe.allowfullscreen = true;
  div.appendChild(iframe);
  let description = document.createElement("div");
  description.classList.add("trailer-description");
  description.innerText = trailer.description;
  div.appendChild(description);
  trailerDiv.appendChild(div);
}

const allTrailers = document.querySelectorAll(".trailer");
const handleLeftClick = () => {
  const nextIndex =
    activeIndex - 1 >= 0 ? activeIndex - 1 : trailers.length - 1;
  const currentTrailer = document.querySelector(
    `.trailer[data-index="${activeIndex}"]`
  );
  const nextTrailer = document.querySelector(
    `.trailer[data-index="${nextIndex}"]`
  );
  currentTrailer.dataset.status = "after";
  nextTrailer.dataset.status = "becoming-active-from-before";
  setTimeout(() => {
    nextTrailer.dataset.status = "active";
    activeIndex = nextIndex;
  }, 200);
};

const handleRightClick = () => {
  const nextIndex = activeIndex + 1 < trailers.length ? activeIndex + 1 : 0;
  const currentTrailer = document.querySelector(
    `.trailer[data-index="${activeIndex}"]`
  );
  const nextTrailer = document.querySelector(
    `.trailer[data-index="${nextIndex}"]`
  );
  currentTrailer.dataset.status = "before";
  nextTrailer.dataset.status = "becoming-active-from-after";
  setTimeout(() => {
    nextTrailer.dataset.status = "active";
    activeIndex = nextIndex;
  }, 200);
};
/*
// Create a YouTube player for each video
function onYouTubeIframeAPIReady() {
    var players = Array.from(document.querySelectorAll('.trailer')).map((video, index) => {
      return new YT.Player(video, {
        videoId: video.dataset.videoId,
        events: {
          'onStateChange': function(event) {
            // If the video is not active, stop it from playing
            if (event.target.getIframe().parentNode.dataset.status !== 'active') {
              event.target.pauseVideo();
              console.log('pause');
            }
          }
        }
      });
    });
  }
  */
