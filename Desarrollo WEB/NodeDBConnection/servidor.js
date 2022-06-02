const express = require('express')
const mysql = require('mysql')
const myconn = require('express-myconnection')

const routes = require('./routes')
const rint = require('./insertar')

const app = express()
app.set('port', process.env.PORT || 9000)
const dbOptions = {
    host: 'localhost',
    port: 3306,
    user: 'root',
    password: '',
    database: 'banco402'
}


// middlewares -------------------------------------
app.use(myconn(mysql, dbOptions, 'single'))
app.use(express.json())

// routes -------------------------------------------
app.get('/', (req, res) => {
    res.send('esta es la pagina de inicio')
})

app.get('/insertar', (req, res) => {
    insertar(result => {
        res.json(result)
    })
    res.send('esta es la pagina de inicio')
})
app.use('/api', routes)
app.use('/guardar', rint)
    // server running -----------------------------------
app.listen(app.get('port'), () => {
    console.log('server running on port', app.get('port'))
})