function onClick (event)
{
  d3.json("/json").then((data)=> {
    var names = data.map(l => l.recipe.label);
    var nameArray = names.filter(eventObj => eventObj.id == event);
    //var nameresult = nameArray[0];
    console.log(nameArray);
    
    var nutrition = data.map(l => l.recipe.totalNutrients);
    var nutriArray = nutrition.filter(eventObj => eventObj.id == event);
    //var nutriresult = nutriArray[0];
    console.log(nutriArray);
  });
}

