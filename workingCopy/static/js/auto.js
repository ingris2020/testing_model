d3.json("/json").then((data)=> {
    
    var recipe_names = data.map(l => l.recipe.label);

    $(function(){
        $("#input").autocomplete({
            source: recipe_names
        });
        var inputElement = d3.select("#input");

        var inputValue = inputElement.property("value");
        console.log(inputValue); 
    });
    

});





