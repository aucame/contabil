
//$.get("http://ipinfo.io", function (response) {
//    $("#ip").html("IP: " + response.ip);
//    $("#address").html("Location: " + response.city + ", " + response.region);
//    $("#details").html(JSON.stringify(response, null, 4));
//}, "jsonp");

//curl 'https://api.ipify.org?format=json'

var app = angular.module('appContabil', ['Config']);

app.controller('ctlContabil', function($scope, $location, $http, $window, config) {

	$scope.linkapi = config.linkapi;
	$scope.versao = config.versao;
	$scope.linksite = config.linksite;

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
				url: 		$scope.linkapi + "/login/" + $scope.user.username,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				
				$scope.dblogin = response.data.cadusuarios;
				$scope.senha = $scope.dblogin[0]['senha'];
				$scope.remoteip = $scope.dblogin[0]['remoteip'];

				if($scope.user.password == $scope.senha){
					$scope.param = angular.toJson($scope.user)
					$window.sessionStorage.setItem('login', $scope.param);
					$window.sessionStorage.setItem('remoteip', $scope.remoteip);
					location.href = $scope.linksite + 'principal.html';
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
