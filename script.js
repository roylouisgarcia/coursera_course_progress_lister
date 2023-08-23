$(document).ready(function () {
  let toggle_elements = document.querySelectorAll(".toggle_courses");

  for (toggle_element of toggle_elements) {
    toggle_element.addEventListener("click", function () {
      if (!this.dataset.clicked) {
        this.setAttribute("data-clicked", "true");
        this.style.backgroundColor = "#fff";
        this.style.color = "#000";
        this.innerHTML = "Hide Courses";
        this.parentElement.nextElementSibling.classList.remove(
          "courses_list_display_none"
        );
        this.parentElement.style.backgroundColor = "#FFA500";
      } else {
        this.removeAttribute("data-clicked");
        this.removeAttribute("style");
        this.parentElement.removeAttribute("style");
        this.parentElement.nextElementSibling.classList.add(
          "courses_list_display_none"
        );
        this.innerHTML = "Show Courses";
      }
    });
  }
});
