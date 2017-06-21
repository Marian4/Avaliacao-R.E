app.controller("avaliarController", function($scope, $mdToast, $state, $stateParams){

    $scope.firstRate = 0;
    $scope.secondRate = 0;
    $scope.readOnly = true;

    $scope.matricula = $stateParams.matricula;
    
    $scope.onItemRating = function(rating){

      var toast = $mdToast.simple()
                    .textContent('Sua avaliação foi computada.')
                    .position('top right')
                    .hideDelay(3000);
      $mdToast.show(toast);

      $state.transitionTo("home", {reload: true});
    };
});
