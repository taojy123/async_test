const express = require('express')
const request = require('request')

const app = express()

app.get('/', (req, res) => {

	request('http://lovegaudi.art:3000', (error, response, body) => {
		res.send('hello')
	})
})

app.listen(5000, () => console.log('Example app listening on port 5000!'))



// apt install npm
// npm install n -g
// n lts
// node app.js


