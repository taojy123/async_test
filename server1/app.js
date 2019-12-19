const express = require('express')
const request = require('request')

const app = express()

app.get('/', (req, res) => {

	request('http://lovegaudi.art:3000', (error, response, body) => {
		res.send('1111')
	})

	//setTimeout(() => {
	//	res.send('2222')
	//}, 3000)
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))



// apt install npm
// npm install n -g
// n lts
// node app.js


