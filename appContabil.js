
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});

var app = angular.module('appContabil', []);

app.controller('ctlContabil', function($scope, $location) {

	$scope.principal = function(user) {

		console.log($scope.user)

		if (user == undefined) {

		}else{
			location.href = 'http://' + $location.host() + '/contabil/principal.html';
		}

	};

});
