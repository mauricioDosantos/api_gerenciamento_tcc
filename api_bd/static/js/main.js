function getData(){
	axios({
		method:'GET',
		url:'127.0.0.1:8000/api/v1/usuarios/',
	});
	.then(function(response){
		document.getElementById('dados').innerHTML = response.data;
		console.log('Passou aqui na resposta!');
	});
}