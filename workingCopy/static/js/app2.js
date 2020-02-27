function onClick (event)
{
  // Read the text from the input field
  var inputElement = d3.select("#input");
  var inputValue = inputElement.property("value");

  // Create a URL for the desired recipe
  var url = "/recipe/"
  var full_url = url + inputValue;

  // Send a request for the recipe
  console.log(`Sending request for ${full_url}`);    
  d3.json(full_url).then((response) => {
    
    // ... and show the response received
    console.log(`${inputValue} returned ${response}`);    

  });
}
  

