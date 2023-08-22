$(document).ready(function () {
  $("#ibm_cybersecurity_analyst_professional_certificate_button").click(function () {
    $("#ibm_cybersecurity_analyst_professional_certificate_list").show(
      "slow",
      function () {}
    );
    $("#ibm_cybersecurity_analyst_professional_certificate_list").removeClass(
      "courses_list_display_none"
    );
    $("#ibm_cybersecurity_analyst_professional_certificate_list").addClass(
      "courses_list_display_flex"
    );
    $("#ibm_cybersecurity_analyst_professional_certificate_list").css(
      "display",
      "flex"
    );
    document.getElementById("ibm_cybersecurity_analyst_professional_certificate_button").innerHTML = "Hide Courses";
  });
});
