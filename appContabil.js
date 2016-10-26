
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

var app = angular.module('appContabil', []);

app.controller('ctlContabil', function($scope, $location, $window) {

	$scope.doGreeting = function(greeting) {
        $window.alert('teste');
      };

	$scope.principal = function(user) {

		if (user == undefined || user.username == undefined || user.password == undefined || user.username == '' || user.password == '' ) {
			swal({title: "", text: "Informe usuario e senha !!!", type: "error"});
		}else{
			$scope.login = angular.toJson($scope.user);
			$window.sessionStorage.setItem('login', $scope.login);

			location.href = 'http://' + $location.host() + '/contabil/principal.html';
		}
		
	};

});
