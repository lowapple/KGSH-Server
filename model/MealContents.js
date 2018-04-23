import { Schema, model } from "mongoose";

var MealContentsScheme = new Schema({
    id_of_meal : Object,
    good : Number,
    bad : Number
}, {
    collection : 'meal_of_contents'
})

var MealContents = model('meal_contents', MealContentsScheme)

module.exports = MealContents