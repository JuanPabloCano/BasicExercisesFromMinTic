const express = require('express')
const app = express()
app.set('port', process.env.PORT || 9000)
app.get('/', (req, res) => {
    res.sendFile('./index.html', { root: __dirname })
})
app.listen(app.get('port'), () => {
    console.log('servidor corriendo en el puerto: ', app.get('port'))
})