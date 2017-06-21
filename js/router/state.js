app.config(function ($stateProvider, $urlRouterProvider) {
    
    // Rota padrão.
    $urlRouterProvider.otherwise("/");
    
    // Estados
    $stateProvider
        .state('home', {
            url: '/',
            templateUrl: 'home.html',
            controller: 'logarController'
        })
        .state('avaliar', {
            url: '/avaliar/:matricula',
            templateUrl: 'avaliar.html',
            controller: 'avaliarController'
        })

});