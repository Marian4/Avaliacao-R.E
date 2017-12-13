app.controller("avaliarController", function($scope, $mdToast, $state, $stateParams, alunoService, respostaService){

    $scope.firstRate = 0;
    $scope.secondRate = 0;
    $scope.readOnly = true;


    $scope.matricula = $stateParams.matricula;
    $scope.perguntas;
    $scope.respostas
    var p;

    var matricula = $scope.matricula;

    respostaService.buscarPerguntas()
        .then(function(response){
            $scope.perguntas = response.data;
            console.log($scope.perguntas);

        });

    console.log($scope.perguntas);



    $scope.onItemRating = function(rating){

      alunoService.buscarAlunoPorMatricula(matricula)
        .then(function(response){

				var aluno = response.data;
				console.log(aluno.id);

				console.log($scope.respostas);
                respostas = {'respostas': $scope.respostas, 'id': aluno.id};
                respostaService.enviarResposta(respostas);

        });







      var toast = $mdToast.simple()
                    .textContent('Sua avaliação foi computada.')
                    .position('top right')
                    .hideDelay(3000);
      $mdToast.show(toast);

      $state.transitionTo("home", {reload: true});
    };

    carregarAluno = function(matricula){
        alunoService.buscarAlunoPorMatricula(matricula)
            .then(function(response){
                $scope.aluno = response.data;
            });

    };

    carregarAluno($scope.matricula);
});
