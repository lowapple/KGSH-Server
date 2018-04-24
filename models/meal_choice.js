var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var MealChoiceScheme = new Schema({
    meal_id : String,
    good : Number,
    bad : Number
}, {
    collection : 'meal_choices'
})

var MealChoice = mongoose.model('meal_choice', MealChoiceScheme)

module.exports = MealChoice