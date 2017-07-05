app.controller("logarController", function($scope, $mdToast, $state, $stateParams, alunoService){
    
    $scope.aluno;

	$scope.validarMatricula = function() {
		
		var matricula = $scope.matricula;
		// Capturar a matrícula.
		// Enviar requisição para o serviço.
		alunoService.buscarAlunoPorMatricula(matricula)
			.then(function(response){
				console.log("Retornou com sucesso!");
				// Encaminha para a página de avaliação.
			})
			.catch(function(data){
				console.log("Retornou com problema!");
			});
		// Analisar resposta.
		$state.transitionTo("avaliar", {
		    matricula: matricula
		});
	}

	$scope.login = function(){
        
        var aluno = $scope.aluno;
		// Capturar a matrícula.
		// Enviar requisição para o serviço.
		alunoService.fazerLogin(aluno)
			.then(function(response){
				aluno = response.data;

				// Encaminha para a página de avaliação.
				$state.transitionTo("avaliar", {
                    matricula: aluno.matricula
                });
			})
			.catch(function(data){
				console.log(data.status);
				var toast = $mdToast.simple()
                    .textContent('Dados de login incorretos, tente novamente.')
                    .position('top right')
                    .hideDelay(3000);
                $mdToast.show(toast);
			});
	}
});