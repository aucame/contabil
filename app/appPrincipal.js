var app = angular.module('appPrincipal',[]);

app.controller('ctlPrincipal', function($scope, $location, $window) {

	$scope.appUsuario = function() {
		location.href = 'http://' + $location.host() + '/contabil/usuario.html';
	};

	$scope.appCliente = function() {
		location.href = 'http://' + $location.host() + '/contabil/cliente.html';
	};

	$scope.appEmpresa = function() {
		location.href = 'http://' + $location.host() + '/contabil/empresa.html';
	};

	$scope.appParametro = function() {
		location.href = 'http://' + $location.host() + '/contabil/parametro.html';
	};

	$scope.appPlano = function() {
		location.href = 'http://' + $location.host() + '/contabil/plano.html';
	};

	$scope.appLancamento = function() {
		location.href = 'http://' + $location.host() + '/contabil/lancamento.html';
	};

	$scope.logout = function() {
		location.href = 'http://' + $location.host() + '/contabil/';
	};

	//$scope.login = angular.fromJson($window.sessionStorage.getItem('login'));
	//console.log('Buscou da sessao = ' + $scope.login.username);

//	$scope.teste = 

	try {
		$scope.login = angular.fromJson($window.sessionStorage.getItem('login'));
		//console.log($scope.login);

		if($scope.login == null){
			$scope.logout();
		};

		} catch(e) {
			console.log('erro');
		};

});
