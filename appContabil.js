
var app = angular.module('appContabil', []);

app.controller('ctlContabil', function($scope, $location) {

	$scope.principal = function(user) {
//		console.log(user)
		location.href = 'http://' + $location.host() + '/contabil/principal.html';
	};

});
