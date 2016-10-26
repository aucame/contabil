
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

var app = angular.module('appContabil', []);

app.controller('ctlContabil', function($scope, $location, $window) {

	$scope.principal = function(user) {

		console.log($scope.user)

		if (user == undefined) {
			//$window.sessionStorage.currentUserId5 = '5';
		}else{
			//$window.sessionStorage.setItem('login', $scope.user);

			$window.sessionStorage.setItem('login', $scope.user.username);
			$window.sessionStorage.setItem('senha', $scope.user.password);
			//location.href = 'http://' + $location.host() + '/contabil/principal.html';

			$scope.login = $window.sessionStorage.getItem('login');
			$scope.senha = $window.sessionStorage.getItem('senha');
			console.log($scope.login);			
			console.log($scope.senha);			
		}

		//alert($window.sessionStorage.currentUserId5);

	};

});
