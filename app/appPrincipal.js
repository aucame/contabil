var app = angular.module('appPrincipal',['Config']);

app.controller('ctlPrincipal', function($scope, $location, $window, config) {

	$scope.local = config.local;

	$scope.appMenu = function(menu) {
		if(menu == 'logout'){
			location.href = $scope.local;
		} else {
			location.href = $scope.local + menu + '.html';
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
