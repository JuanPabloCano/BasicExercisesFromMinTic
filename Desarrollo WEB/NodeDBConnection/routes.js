const express = require('express')
const routes = express.Router()

routes.get('/', (req, res) => {
    req.getConnection((err, conn) => {
        if (err) return res.send(err)

        conn.query('SELECT * FROM registro', (err, rows) => {
            if (err) return res.send(err)

            res.json(rows)
        })
    })
})
routes.get('/guardar', (req, res) => {
    req.getConnection((err, conn) => {
        if (err) return res.send(err)
        conn.query('INSERT INTO registro value(null, "nada", "65685f", "nombre primera mascota", "firu")', [req.body], (err, rows) => {
            if (err) return res.send(err)

            res.send('registro guardado')
        })
    })
})


routes.post('/', (req, res) => {
    req.getConnection((err, conn) => {
        if (err) return res.send(err)
        conn.query('INSERT INTO registro set ?', [req.body], (err, rows) => {
            if (err) return res.send(err)

            res.send('registro guardado')
        })
    })
})

routes.delete('/:id', (req, res) => {
    req.getConnection((err, conn) => {
        if (err) return res.send(err)
        conn.query('DELETE FROM registro WHERE id = ?', [req.params.id], (err, rows) => {
            if (err) return res.send(err)

            res.send('registro eliminado')
        })
    })
})

routes.put('/:id', (req, res) => {
    req.getConnection((err, conn) => {
        if (err) return res.send(err)
        conn.query('UPDATE registro set ? WHERE id = ?', [req.body, req.params.id], (err, rows) => {
            if (err) return res.send(err)

            res.send('registro acualizado')
        })
    })
})

routes.get('/', (req, res) => {
    res.send("esoto es una pruba")
})

module.exports = routes