
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

var app = angular.module('appContabil', []);

app.controller('ctlContabil', function($scope, $location, $window) {

	//$scope.doGreeting = function(greeting) {
    //    $window.alert('teste');
    //};

	$scope.principal = function(user) {
//		$scope.login = angular.toJson($scope.user);

		$scope.user = {"username": "admin", "password": "admin"}

		if ($scope.user == undefined || 
		    $scope.user.username == undefined || 
			$scope.user.password == undefined ||  
			$scope.user.username == '' || 
			$scope.user.password == '' ) {
			swal({title: "", text: "Informe usuario e senha !!!", type: "error"});
		}else{
			$scope.param = angular.toJson($scope.user)
			$window.sessionStorage.setItem('login', $scope.param);
			location.href = 'http://' + $location.host() + '/contabil/principal.html';
		}
		
	};

	$window.sessionStorage.removeItem('login');

});
