function submitOrder() { 
  const form = document.querySelector("form");
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const username = form.elements.username.value;
    const burgerQty = form.elements.burgerQty.value;
    const softDrink = form.elements.softDrink.value;

    const receipt = document.querySelector("#receipt");
    receipt.style.display = "block";

    document.querySelector("#receipt-username").textContent = username;
    document.querySelector("#receipt-burger-qty").textContent = burgerQty;
    document.querySelector("#receipt-soft-drink").textContent = softDrink;

    const totalCost = burgerQty * 2 + (softDrink === "Yes" ? 0.5 : 0);
    document.querySelector("#receipt-total-cost").textContent =
      totalCost.toFixed(2);
  });
  // Validate
  const username = document.querySelector("#username").value;
  const burgerQty = document.querySelector("#burgerQty").value;

  let isValid = true;
  let errorMessage = "";

  if (!username) {
    isValid = false;
    errorMessage = "Username cannot be blank.";
  } else if (burgerQty < 1) {
    isValid = false;
    errorMessage = "Burger quantity must be at least 1.";
  }

  if (isValid) {
    // display the receipt
    document.querySelector("#receipt").style.display = "block";

    document.getElementById("receipt").style.display = "block";
    document.querySelector("#receipt-username").innerHTML = username;
    document.querySelector("#receipt-burger-qty").innerHTML = burgerQty;
    document.querySelector("#receipt-soft-drink").innerHTML =
    
    document.querySelector("#softDrink").value;
    document.querySelector("#receipt-total-cost").innerHTML = alert(
      "Thank you for ordering!"
    );
    "$" + (burgerQty * 10 + 2);
  } else {
    // display the error message
    document.querySelector("#username-error").innerHTML = errorMessage;
  }
}
