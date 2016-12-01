var app = angular.module('appPrincipal',['Config']);

app.controller('ctlPrincipal', function($scope, $location, $window, config) {

	$scope.local = config.local;

	$scope.appUsuario = function() {
		location.href = $scope.local + 'usuario.html';
	};

	$scope.appCliente = function() {
		location.href = $scope.local + 'cliente.html';
	};

	$scope.appEmpresa = function() {
		location.href = $scope.local + 'empresa.html';
	};

	$scope.appParametro = function() {
		location.href = $scope.local + 'parametro.html';
	};

	$scope.appPlano = function() {
		location.href = $scope.local + 'plano.html';
	};

	$scope.appLancamento = function() {
		location.href = $scope.local + 'lancamento.html';
	};

	$scope.logout = function() {
		location.href = $scope.local;
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
