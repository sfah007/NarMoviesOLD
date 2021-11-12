function Search(){
    if(document.getElementById("search-input").value !== ""){
    window.location.href = "/search?q=" + document.getElementById("search-input").value;
    }
  }

  document.getElementById("search-input")
  .addEventListener("keyup", function(event) {
  event.preventDefault();
  if(document.getElementById("search-input").value !== ""){
    if (event.keyCode === 13) {
      document.getElementById("search-btn").click();
    }
  }
});