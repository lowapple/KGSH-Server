var Meal = require('../models/meal')
var MealChoice = require('../models/meal_choice')

function defaultErrorHandling(err, res) {
    return res.status(500).send({error : 'database failure'});
}

module.exports = function(app) {
    app.get('/api/meal/:date', function(req, res){
        date = req.params.date
        Meal.findOne({
            'date' : date
        }, (err, meal) => {
            if(err) 
                return defaultErrorHandling(err, res)
            
            console.log(meal)                            
            res.json(meal)
        });
    });

    app.get('/api/meal/choice/:choice_id', function(req, res){
        choice_id = req.params.choice_id
        MealChoice.find({ 
            '_id' : choice_id
        }, (err, choice)=> {
            if(err) 
                return defaultErrorHandling(err, res)

            console.log(choice);
            res.json(choice)
        }).limit(20);
    });
}