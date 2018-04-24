var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var MealScheme = new Schema({
    date : String,
    week : String,
    contents : Array,
}, {
    collection : 'meals'
})

var Meal = mongoose.model('meal', MealScheme)

module.exports = Meal