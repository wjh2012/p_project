const express = require('express');
const app = express();
const PORT = 3000

const mysql = require('mysql');
const dbconfig = require('./database.js');
const connection = mysql.createConnection(dbconfig);

app.get('/:val/:centi', (req,res)=>{
    var part = String(req.params.val)
    var size = parseFloat(req.params.centi)

    var sql = 'SELECT * FROM pants WHERE id in (SELECT DISTINCT id FROM pants_size WHERE '+part +' BETWEEN ' + String(size-1) +' AND '+String(size+1)+') order by sales desc'
    connection.query(sql, (err,result)=>{
        if (err){
            console.log(err)
        }
        
        console.log(result)
        res.json(result)
    })
})

app.listen(PORT, () => {
    console.log('server is running on port' + PORT)
})