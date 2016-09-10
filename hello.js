
var app = angular.module('demo', []);

app.controller('Hello', function($scope, $http) {

    var chamada = function () {
        $http({
        method: 'GET',
        //url: 'http://200.98.174.103:8080/usuarios'
        url: 'http://127.0.0.1:8080/usuarios'
        }).then(function(response) {
            console.log(response.data);
            $scope.greeting = response.data;
        }, function(response) {
            console.log('Não foi possível obter os dados: ' + response.data);
        });
    }

    chamada();

});

