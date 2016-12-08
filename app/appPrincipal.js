var app = angular.module('appPrincipal',['Config']);

app.controller('ctlPrincipal', function($scope, $location, $window, config) {

	$scope.linksite = config.linksite;

	$scope.appMenu = function(menu) {
		if(menu == 'logout'){
			location.href = $scope.linksite;
		} else {
			location.href = $scope.linksite + menu + '.html';
		}
	};

	//$scope.login = angular.fromJson($window.sessionStorage.getItem('login'));
	//console.log('Buscou da sessao = ' + $scope.login.username);

//	$scope.teste = 

	try {
		$scope.login = angular.fromJson($window.sessionStorage.getItem('login'));
		//$scope.remoteip = $window.sessionStorage.getItem('remoteip');
		//console.log($scope.login);

		if($scope.login == null){
			$scope.logout();
		};

		} catch(e) {
			console.log(e.message);
		};

});
