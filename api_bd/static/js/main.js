//const axios = require('axios').default;
function getData(){
	axios({
		method:'GET',
		url:'http://127.0.0.1:8000/api/v1/usuarios/',  //responseType vem por default json
	})
	.then(function(response){
		document.getElementById('dados').innerHTML = response.data;
		console.log('Passou aqui na resposta!');
	});
}