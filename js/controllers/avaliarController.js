app.controller("avaliarController", function($scope, $mdToast){

	$scope.firstRate = 0;
    $scope.secondRate = 3;
    $scope.readOnly = true;
    
    $scope.onItemRating = function(rating){

      var toast = $mdToast.simple()
                    .textContent('Mensagem que Mariana queria.')
                    .position('top right')
                    .action('Ok')
                    .hideDelay(6000);
      $mdToast.show(toast);

    };
});
