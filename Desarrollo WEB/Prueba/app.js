const { response } = require('express');
const express = require('express');
const app = express();
app.get('/Ping', (request, response) => {
    response.send('esto es una prueba');
});

app.get('/myPath', function(req, res, next) { response.send('esto es una prueba');});
app.listen(9090, 'localhost');