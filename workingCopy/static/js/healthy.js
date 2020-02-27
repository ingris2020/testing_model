function displayHealth(recipeObject)
{
      /*Diplay Recipe Name */
   d3.json("/json").then((data)=> {
  
    var nutrition = data.map(l => l.recipe.totalNutrients);
    console.log (nutrition);
});

    var x = [] //list of values (X1, X2, X3...)

    //Generates x list. If nutrition value doesnt exist for recipe, enter a 0
    try{
         x.push(nutrition.ENERC_KCAL.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.FAT.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.FASAT.quantity )
    }
    catch{
        x.push(0)
    }
    try{
        x.push(rnutrition.FATRN.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.FAMS.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.FAPU.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.CHOCDF.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.FIBTG.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.SUGAR.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.PROCNT.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.CHOLE.quantity)
    }
    catch{
        x.push(0)
    }
    try{
        x.push(nutrition.NA.quantity)
    }
    catch{
        x.push(0)
    }
    

    //model equation 1
    d3.json("notebook/modelD1.json").then((model)=> {

        // logistic regression equation = 
        // e^(B0 + B1X1 + B2X2 + B3X3...)/1 + e^(B0 + B1X1 + B2X2 + B3X3...)
        var coeffs = model.coefficients; //list of coefficients (B1, B2, B3...)
        var inter = model.intercept  // intercept B0
       
        //Calculate (B1X1 + B2X2 + B3X3...BnXn)
        var BX_total = 0

        for(i=0; i < x.length; i++) {

            BX_total = coeffs[i]*x[i] + BX_total

        }
        
        // P = e^(B0 + B1X1 + B2X2 + B3X3...)/1 + e^(B0 + B1X1 + B2X2 + B3X3...)
       var exp_total = +inter + +BX_total 
       
       var predict = Math.exp(exp_total) /(1+Math.exp(exp_total))

       // if P >= 0.5 then recipe is healthy. else if p < 0.5 then recipe unhealthy

       if (predict >= 0.5) {
           var result = "Recommended"
       }
       else{
           var result = "Not Good for You"
       }
    
        console.log("David predict", result)
    })

     //model equation 2
     d3.json("notebook/modelD1.json").then((model)=> {

        // logistic regression equation = 
        // e^(B0 + B1X1 + B2X2 + B3X3...)/1 + e^(B0 + B1X1 + B2X2 + B3X3...)
        var coeffs = model.coefficients; //list of coefficients (B1, B2, B3...)
        var inter = model.intercept  // intercept B0
       
        //Calculate (B1X1 + B2X2 + B3X3...BnXn)
        var BX_total = 0

        for(i=0; i < x.length; i++) {

            BX_total = coeffs[i]*x[i] + BX_total

        }
        
        // P = e^(B0 + B1X1 + B2X2 + B3X3...)/1 + e^(B0 + B1X1 + B2X2 + B3X3...)
       var exp_total = +inter + +BX_total 
       
       var predict = Math.exp(exp_total) /(1+Math.exp(exp_total))

       // if P >= 0.5 then recipe is healthy. else if p < 0.5 then recipe unhealthy
        
       if (predict >= 0.5) {
           var result = "Recommended"
       }
       else{
           var result = "Not Good for You"
       }
    
        console.log("Cindy predict", result)
    })
}