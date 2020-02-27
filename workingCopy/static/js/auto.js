d3.json("/json").then((data)=> {
    
    var recipe_names = data.map(l => l.recipe.label);
    var nutrition = data.map(l => l.recipe.totalNutrients);
    var nutrition = data.map(l => l.recipe.totalNutrients);
    console.log();
    
    $(function(){
        $("#input").autocomplete({
            source: recipe_names
        });
        var inputElement = d3.select("#input");

        var inputValue = inputElement.property("value");
        console.log(inputValue); 
    });
    

});





