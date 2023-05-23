const api = "http://127.0.0.1:5000";

window.onload = () => {
  // BEGIN CODE HERE
  // Code to execute when the window is loaded
  // For example, you can fetch initial data or perform any necessary setup
  // END CODE HERE
};

searchButtonOnClick = () => {
  // BEGIN CODE HERE
  const searchInput = document.getElementById("searchInput").value;

  fetch(`${api}/search?query=${searchInput}`)
    .then(response => response.json())
    .then(data => {
      const table = document.getElementById("searchResultsTable");
      table.innerHTML = `
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Production</th>
          <th>Price</th>
          <th>Color</th>
          <th>Size</th>
        </tr>
      `;

      data.forEach(product => {
        table.innerHTML += `
          <tr>
            <td>${product.id}</td>
            <td>${product.name}</td>
            <td>${product.production}</td>
            <td>${product.price}</td>
            <td>${product.color}</td>
            <td>${product.size}</td>
          </tr>
        `;
      });

      const searchResultsTitle = document.getElementById("searchResultsTitle");
      searchResultsTitle.textContent = "Search Results:";
    })
    .catch(error => {
      console.error("Error:", error);
    });
  // END CODE HERE
};

productFormOnSubmit = (event) => {
  // BEGIN CODE HERE
  event.preventDefault();

  const nameInput = document.getElementById("nameInput").value;
  const productionInput = document.getElementById("productionInput").value;
  const priceInput = document.getElementById("priceInput").value;
  const colorInput = document.getElementById("colorInput").value;
  const sizeInput = document.getElementById("sizeInput").value;

  const product = {
    name: nameInput,
    production: productionInput,
    price: priceInput,
    color: colorInput,
    size: sizeInput
  };

  fetch(`${api}/add-product`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(product)
  })
    .then(response => response.json())
    .then(data => {
      console.log("Success:", data);
      alert("Product added successfully");
      // Reset the form
      document.getElementById("addProductForm").reset();
    })
    .catch(error => {
      console.error("Error:", error);
      alert("An error occurred while adding the product");
    });
  // END CODE HERE
};
