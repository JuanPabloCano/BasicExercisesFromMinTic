const express = require('express')
const rin = express.Router()

rin.get('/', (req, res) => {
    req.getConnection((err, conn) => {
        if (err) return res.send(err)
        else conn.query('INSERT INTO registro value(null, "upb23", "123456789", "nombre primera mascota", "bolivariana")', [req.body], (err, rows) => {
                if (err) return res.send(err)

                else res.send('registro guardado')

            }

        )
    })
})



module.exports = rin