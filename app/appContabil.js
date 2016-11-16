
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

var app = angular.module('appContabil', ['Config']);

app.controller('ctlContabil', function($scope, $location, $http, $window, config) {

	$scope.http = config.link;
	$scope.versao = config.versao;

	$scope.principal = function(user) {

		$scope.user = {
			"username": "admin",
			"password": "admin"
		};

		if ($scope.user == undefined || 
		    $scope.user.username == undefined || 
			$scope.user.password == undefined ||  
			$scope.user.username == '' || 
			$scope.user.password == '' ) {
			swal({title: "", text: "Informe usuario e senha !!!", type: "error"});
		}else{

			$http({
				method: 	"GET",
				url: 		$scope.http + "/login/" + $scope.user.username,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				
				$scope.dblogin = response.data.cadusuarios;
				$scope.senha = $scope.dblogin[0]['senha'];

				console.log($scope.senha);

				if($scope.user.password == $scope.senha){
					$scope.param = angular.toJson($scope.user)
					$window.sessionStorage.setItem('login', $scope.param);
					location.href = 'http://' + $location.host() + '/contabil/principal.html';
				}else{
					swal({title: "", text: "Senha invalida !!!", type: "error"});
				}				

			}, function(error){
				console.log("Error... = " + error.status);
			});

		}
		
	};

	$window.sessionStorage.removeItem('login');

});
