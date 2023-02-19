// a. Roll number is a 7-digit numeric value
// b. Name should be an alphabetical value (String)
// c. Non-empty and valid fields like DOB

function validateForm() {
  var rollNumber = document.forms["registrationForm"]["rollNumber"].value;
  var name = document.forms["registrationForm"]["name"].value;
  var email = document.forms["registrationForm"]["email"].value;

  if (rollNumber == "" || isNaN(rollNumber) || rollNumber.length != 7) {
    alert("Please enter a valid 7-digit roll number");
    return false;
  }

  if (!/^[a-zA-Z]*$/g.test(name)) {
    alert("Please enter a valid name");
    return false;
  }

  if (email == "" || !/\S+@\S+\.\S+/.test(email)) {
    alert("Please enter a valid email address");
    return false;
  }

  return true;
}
