document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();

  var isValidName = validateName();
  var isValidRoll = validateRoll();
  var isValidGender = validateGender();
  var isValidAlphabeticalName = validateAlphabeticalName();

  if (isValidName && isValidRoll && isValidGender && isValidAlphabeticalName) {
    form.submit();
  }
});
