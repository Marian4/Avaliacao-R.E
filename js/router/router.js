app.config(function ($routeProvider, $locationProvider) {

    // Remover a exclamação (!) da URL
    var SEM_PREFIXO = '';
    $locationProvider.hashPrefix(SEM_PREFIXO);

    $routeProvider
        .when("/", {
            templateUrl: "views/home.html",
			controller: "ctrlHome"

        });
    $routeProvider
        .when("/avaliacao", {
            templateUrl: "views/avaliacao.html",
			controller: "ctrlAvaliacao"
        });
});