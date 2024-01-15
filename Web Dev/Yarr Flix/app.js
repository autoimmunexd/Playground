// API Key
const API_KEY = "425fddc64b3d3249cc9836076ed8eba2";

// API URLs
const API_URL = `https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=${API_KEY}&page=1`;
const SEARCH_API = `https://api.themoviedb.org/3/search/movie?api_key=${API_KEY}&query=`;
const IMG_PATH = "https://image.tmdb.org/t/p/w1280";

// DOM Elements
const form = document.querySelector("form");
const main = document.querySelector("main");
const search = document.getElementById("search");
const container = document.querySelector(".container");

// Initial movie display
getMovies(API_URL);

// Function to fetch movies from API
async function getMovies(url) {
  const resp = await fetch(url);
  const respData = await resp.json();

  showMovies(respData.results);
}

// Function to display movies in the DOM
function showMovies(movies) {
  main.innerHTML = "";

  movies.forEach((movie) => {
    const { poster_path, title, vote_average, release_date, overview, backdrop_path, id } = movie;

    const movieEl = document.createElement("div");
    movieEl.classList.add("movie");
    movieEl.setAttribute("data-id", `${id}`);

    movieEl.innerHTML = `
      <img src="${IMG_PATH + poster_path}" alt="${title}"/>
      <div class="primary-info">
        <h3>${title}</h3>
        <div class="secondary-info">
          <p class="date">${convertTime(release_date)}</p>
          <span class="${getClassByRate(vote_average)}">${vote_average}</span>
        </div>
      </div>
    `;

    main.appendChild(movieEl);

    movieEl.addEventListener("click", () => {
      container.classList.add("show");
      container.style.backgroundImage = `linear-gradient(to bottom, rgba(0, 0, 0, 0.8) 0%, rgba(0, 0, 0, 0.8) 100%), url(${IMG_PATH + backdrop_path})`;

      container.innerHTML = `
        <img src="${IMG_PATH + poster_path}" alt="${title}"/>
        <div class="wrapper">
          <h1>${title} <span class="light-text">(${convertOnlyYear(release_date)})</span></h1>
          <div class="rate">
            <span class="${getClassByRate(vote_average)}">${vote_average}</span>
          </div>
          <div class="overview">
            <h3>Overview</h3>
            <p>${overview}</p>
          </div>
          <div class="date">
            <p class="date"><span class="thick-text">Release date:</span> ${convertTime(release_date)}</p>
          </div>
        </div>
      `;
    });
  });
}

// Function to convert date to specific format
const convertOnlyYear = (time) => {
  return new Date(time).toLocaleDateString("en-us", { year: "numeric" });
};

const convertTime = (time) => {
  return new Date(time).toLocaleDateString("en-us", { year: "numeric", month: "long", day: "numeric" });
};

// Event listener for form submission
form.addEventListener("submit", (e) => {
  e.preventDefault();

  const searchTerm = search.value;

  if (searchTerm) {
    getMovies(SEARCH_API + searchTerm);
    search.value = "";
    container.classList.remove("show");
  }
});

// Function to get CSS class based on rating
function getClassByRate(vote) {
  if (vote >= 8) {
    return "green";
  } else if (vote >= 5) {
    return "orange";
  } else {
    return "red";
  }
}