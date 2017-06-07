app.controller("avaliarController", function($scope, $mdToast){

	$scope.firstRate = 0;
    $scope.secondRate = 0;
    $scope.readOnly = true;
    
    $scope.onItemRating = function(rating){

      var toast = $mdToast.simple()
                    .textContent('Sua avaliação foi computada.')
                    .position('top right')
                    .hideDelay(3000);
      $mdToast.show(toast);

    };
});
