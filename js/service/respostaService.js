app.factory("respostaService", function($http, config){

	var _path = config.baseUrl() + "/aluno"; // Endereço do serviço.

	var _enviarResposta = function(resposta){
	    return $http.post(_path + "/resposta", resposta)
	};

	var _buscarPerguntas = function(){
	    return $http.get(_path + "/perguntas")
	};


	return {
		enviarResposta:_enviarResposta ,
		buscarPerguntas:_buscarPerguntas
	};

});