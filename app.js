var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

var db = mongoose.connection;
db.once('open', function(){
    console.log('Connected to mongod server');
});

mongoose.connect('mongodb://localhost/kgsh');

app.use(bodyParser.urlencoded({extended : true}));
app.use(bodyParser.json());

var port = process.env.port || 8080;
var router = require('./routes/meal')(app)

var server = app.listen(port, function(){
    console.log('Anilow server has started on port ' + port);
});