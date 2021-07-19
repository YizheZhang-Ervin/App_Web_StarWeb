let express = require('express');
let vm = require("vm");
let exec = require('child_process').exec;
// var userQuery = require('./models');

let router = express.Router();

/* GET from DB */
// router.get('/api/users', function(req, res, next) {
//     let sql = "select * from nodebook.users";
//     userQuery.queryAll(sql,function(err,rows,fields){
//         console.log(rows);
//     });
// });

router.get('/', function(req, res, next) {
    res.render("index");
});

router.post('/api/js/', function(req, res, next) {
    let codes = JSON.parse(req.body["key"]);
    res.status(200);
    res.json({
      result: JSON.stringify(codes)
    });
});

module.exports = router;