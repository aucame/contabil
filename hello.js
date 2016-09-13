
var app = angular.module('demo', []);

app.controller('Hello', function($scope, $http) {

    var chamada = function () {
        $http({
        method: 'GET',
        url: 'http://200.98.174.103:8080/usuarios/0'
        }).then(function(response) {
            console.log(response.data);
            $scope.retorno = response.data;
        }, function(response) {
            console.log('Não foi possível obter os dados: ' + response.data);
        });
    }

    //chamada();

});

// http://stackoverflow.com/questions/35254742/tornado-server-enable-cors-requests
