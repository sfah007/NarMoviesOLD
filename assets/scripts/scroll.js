scrollBy = 300
function Left(elem) {
  elem.parentElement.scrollLeft -= scrollBy;
  console.log("Scrolled")
}

function Right(elem) {
  elem.parentElement.scrollLeft += scrollBy;
  console.log("Scrolled")
}
