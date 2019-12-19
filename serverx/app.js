const express = require('express')
const app = express()

app.get('/', (req, res) => {
	setTimeout(() => {
		res.send('ok')
	}, 20000)
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))


// apt install npm
// npm install n -g
// n lts
// node app.js

// => http://lovegaudi.art:3000


