const express = require("express");
const fetch = require("node-fetch");
const url = require("url");

const fs = require("fs");

let featured = JSON.parse(fs.readFileSync("assets/featured.json"));
let movies = JSON.parse(fs.readFileSync("Databases/EgybestAllMovies.json"));
let series = JSON.parse(fs.readFileSync("Databases/EgybestAllSeries.json"));

var app = express(); 
app.set("view engine", "ejs");
app.use("/assets", express.static("assets"));


app.get("/home", function (req, res) {
  res.render("home", { data: GetHomeData(), featured: featured["featured"] });
});

app.get(
  "/movies-list",
  GetmoviesByGenre(),
  paginatedResults(),
  function (req, res) {
    if (res.paginatedResults["results"].length == 0) {
      return res.redirect('*');
    }
    return res.render("list", {
      data: res.paginatedResults["results"],
      pages: res.pages,
    });
  }
);

app.get(
  "/search",
  Search(),
  paginatedResults(),
  function (req, res) {
    if (res.paginatedResults["results"].length == 0) {
      return res.redirect('*');
    }
    return res.render("list", {
      data: res.paginatedResults["results"],
      pages: res.pages,
    });
  }
);


app.get("/movie/:id", function (req, res) {
  data = GetMovieByID(req.params.id);
  title = data["title"];
  GetBackDrop(title).then((backdrop) =>
    GetStreamLinks(data["str"]).then((sources) =>
      res.render("movie", { movie: data, backdrop: backdrop, streams: sources })
    )
  );
});

//Get Data For All The Sliders Of Home Page
function GetHomeData() {
  data = {
    "movies-latest": movies.slice(0, 40),
    "movies-action": [],
    "movies-drama": [],
    "movies-animation": [],
  };
  for (let i = 0; i < movies.length; i++) {
    if (
      data["movies-action"].length == 20 &&
      data["movies-drama"].length == 20 &&
      data["movies-animation"].length == 20
    ) {
      return data;
    }
    if (
      movies[i]["genres"].includes("اكشن") &&
      data["movies-action"].length <= 20
    ) {
      data["movies-action"].push(movies[i]);
      continue;
    }
    if (
      movies[i]["genres"].includes("دراما") &&
      data["movies-drama"].length <= 20
    ) {
      data["movies-drama"].push(movies[i]);
      continue;
    }
    if (
      movies[i]["genres"].includes("كرتون") &&
      data["movies-animation"].length <= 20
    ) {
      data["movies-animation"].push(movies[i]);
      continue;
    }
  }
  return data;
}
//Get One Movie Data By Its ID
function GetMovieByID(id) {
  for (let i = 0; i < movies.length; i++) {
    if (movies[i]["_id"] === id) {
      return movies[i];
    }
  }
  return res.redirect('*');;
}
//Get A List Of Movies By A Genre
function GetmoviesByGenre() {
  return (req, res, next) => {
    results = [];
    genre = req.query.genre || "الكل";
    if (genre == "الكل") {
      req.results = movies;
      next();
    }
    for (let i = 0; i < movies.length; i++) {
      if (movies[i]["genres"].includes(req.query.genre)) {
        results.push(movies[i]);
      }
    }

    req.results = results;
    next();
  };
}
//Returns The URL Of The BackDrop Of A Given Movie Title Using TMDB Api
function GetBackDrop(title) {
  return fetch(
    `https://api.themoviedb.org/3/search/movie?query=${title}&page=1&language=en&include_adult=false&region=US&api_key=5ab3893ea126a4e4de407c8158afec96`
  )
    .then((response) => response.json())
    .then((json) => json["results"][0]["backdrop_path"])
    .catch((error) => error);
}
//Returns Stream Sources For A Given Link
function GetStreamLinks(link) {
  return fetch(link)
    .then((response) => response.json())
    .then((json) => json["sources"])
    .catch((error) => error);
}
//Pagination MiddleWare
function paginatedResults() {
  return (req, res, next) => {
    model = req.results;

    const page = parseInt(req.query.page) || 1;
    const limit = parseInt(req.query.limit) || 35;

    const startIndex = (page - 1) * limit;
    const endIndex = page * limit;

    const results = {};
    const pages = {};
    if (page > 2) {
      pages.firstPage = {
        index: 1,
        url: GetPageLink(req, 1),
      };
    }
    pages.currentPage = { index: page, url: GetPageLink(req, page) };

    if (pages.currentPage.index < parseInt(model.length / limit)) {
      pages.lastPage = {
        index: parseInt(model.length / limit + 1),
        url: GetPageLink(req, parseInt(model.length / limit + 1)),
      };
    }
    if (endIndex < model.length) {
      pages.nextPage = {
        index: page + 1,
        url: GetPageLink(req, page + 1),
      };
    }

    if (startIndex > 0) {
      pages.previousPage = {
        index: page - 1,
        url: GetPageLink(req, page - 1),
      };
    }
    try {
      results.results = model.slice(startIndex, endIndex);
      res.paginatedResults = results;
      res.pages = pages;
      next();
    } catch (e) {
      res.status(500).json({ message: e.message });
    }
  };
}
//Returns A Link To A List Page For A Given PageIndex
function GetPageLink(req, pageIndex) {
  if (Object.keys(req.query).length === 0) {
    var searchParams = new URLSearchParams("?" + "page=1");
  } else {
    var searchParams = new URLSearchParams(
      "?" + req.originalUrl.split()
    );
  }
  searchParams.set("page", pageIndex);
  var newRelativePathQuery =
    url.parse(req.url).pathname + "?" + searchParams.toString();
  return newRelativePathQuery;
}
function Search(){
  return (req, res, next) => {
    results = [];
    searchTerm = req.query.q.replace(/ /g,'').toLowerCase()
    for (let i = 0; i < movies.length; i++) {
      if (movies[i]["title"].replace(/ /g,'').toLowerCase().includes(searchTerm)) {
        results.push(movies[i]);
      }
    }
    for (let i = 0; i < series.length; i++) {
      if (series[i]["title"].replace(/ /g,'').toLowerCase().includes(searchTerm)) {
        results.push(series[i]);
      }
    }
    req.results = results;
    next();
  };
}

//Handle 404 Errors
app.get("*", function (req, res) {
  return res.send("404", 404);
});

const port = 8080;
app.listen(port);
