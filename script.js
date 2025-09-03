fetch("courses.json")
  .then(response => response.json())
  .then(courses => {
    console.log(courses);
    const container = document.getElementById("courses-container");

    courses.forEach(course => {
      const courseCard = document.createElement("div");
      courseCard.classList.add("course-card");

      courseCard.innerHTML = `
        <img src="${course.image}" alt="${course.title}">
        <div class="course-content">
          <h3>${course.title}</h3>
          <p>${course.description}</p>
          <p>${course.hours}</p>
           <p>${course.student}</p>
        </div>
      `;

      container.appendChild(courseCard);
    });
  })
  .catch(error => console.error("Error loading courses:", error));
  let myupimg = document.querySelector(".up-img");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    myupimg.style.display = "block";
  } else {
    myupimg.style.display = "none";
  }
}
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


