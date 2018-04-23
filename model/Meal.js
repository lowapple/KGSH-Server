import { Schema, model } from 'mongoose';

var MealScheme = new Schema({
    date : Date,
    meal_of_num : Number,
    contents : String,
}, {
    collection : 'meals'
})

var Meal = model('meal', MealScheme)

module.exports = Meal