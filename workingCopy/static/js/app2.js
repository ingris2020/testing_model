

function onClick (event)
{
   /*Diplay Recipe Name */
  // d3.json("/json").then((data)=> {
      
    //  var names = data.map(l => l.recipe.label);
    //console.log(names); 
    var inputElement = d3.select("#input");

    var inputValue = inputElement.property("value");
    console.log("on click method");
   //var nutrition = data.map(l => l.recipe.totalNutrients);
   //console.log (nutrition);
  //});
    var url = "/recipe/"
    var full_url = url + inputValue;
    console.log(full_url);
    
    d3.json(full_url).then((data) => {
    
      console.log(data);
    
  });
  
 
}
  

