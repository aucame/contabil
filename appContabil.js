
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

var app = angular.module('appContabil', []);

app.controller('ctlContabil', function($scope, $location, $window) {

	$scope.doGreeting = function(greeting) {
        $window.alert('teste');
      };

	$scope.principal = function(user) {

		$scope.login = angular.toJson($scope.user);
		$window.sessionStorage.setItem('login', $scope.login);

		if (user == undefined) {
			//$window.sessionStorage.currentUserId5 = '5';
		}else{
			location.href = 'http://' + $location.host() + '/contabil/principal.html';
		}
		
	};

});
