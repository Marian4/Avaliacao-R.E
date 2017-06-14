app.factory("alunoService", function($http, config){

	var _path = config.baseUrl() + "/aluno"; // Endereço do serviço.

	var _buscarAlunoPorMatricula = function (matricula){
		return $http.get(_path + "/consultar/matricula/" + matricula)
	};
	
	var _fazerLogin = function (aluno){
		return $http.post(_path + "/login", aluno)
	};
	
	return {
		buscarAlunoPorMatricula: _buscarAlunoPorMatricula,
		fazerLogin: _fazerLogin
	};

});