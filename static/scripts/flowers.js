console.log("hello");

const flowerDivs = document.querySelectorAll(".flower");

function displayColour(e) {
  if (
    e.currentTarget.style.backgroundColor === e.currentTarget.style.borderColor
  ) {
    e.currentTarget.style.backgroundColor = "#333";
  } else {
    e.currentTarget.style.backgroundColor = e.currentTarget.style.borderColor;
  }
}

flowerDivs.forEach((f) => {
  return f.addEventListener("click", displayColour);
});

/* 
// dan's work
function toggleColour(event) {
  if (
    event.currentTarget.style.backgroundColor ==
    event.currentTarget.style.borderColor
  ) {
    event.currentTarget.style.backgroundColor = "#333333";
  } else {
    event.currentTarget.style.backgroundColor =
      event.currentTarget.style.borderColor;
  }
}

document.querySelectorAll(".flower").forEach((f) => {
  f.addEventListener("click", toggleColour);
});
*/
