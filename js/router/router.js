app.config(function ($routeProvider, $locationProvider) {

    // Remover a exclamação (!) da URL
    var SEM_PREFIXO = '';
    $locationProvider.hashPrefix(SEM_PREFIXO);

    $routeProvider
        .when("/", {
            templateUrl: "home.html"
        })
});
/*acho q pra fazer com o da avaliação vc tem q separar o css dele e tbm tirar a ag html e deixar só o conteúdo (y)*/