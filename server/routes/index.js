const { json } = require('express');
const express = require('express')
const router = express.Router()

const mysql = require('mysql');
const dbconfig = require('../database.js');
const connection = mysql.createConnection(dbconfig);

connection.connect()

router.get('/:val/:centi', (req,res)=>{
    var part = req.params.val
    var size = parseFloat(req.params.centi)

    var sql = 'SELECT * FROM pants WHERE id in (SELECT DISTINCT id FROM pants_size WHERE '+String(part) +' BETWEEN ' + String(size-1) +' AND '+String(size+1)+') order by sales desc'
    connection.query(sql, (err,result)=>{
        if (err){
            console.log(err)
        }
        
        console.log(result)
        res.json(result)
    })
})

module.exports = router