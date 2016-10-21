
var app = angular.module('appUsuarios', ['ui.grid']);

app.controller('ctlUsuarios', function($scope, $http, $location) {

//17520520

	//$scope.http = "http://200.98.174.103:8080";
	$scope.http = "http://127.0.0.1:8080";

	$scope.usuario = { 
		'idusuario': undefined, 
		'nome': undefined, 
		'senha': undefined, 
		'ativo': 0 
	};

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idusuario', enableCellEdit: false, minWidth: 50, width: 90, displayName: 'Codigo' },
			{ field: 'nome', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Nome' },
			{ field: 'ativo', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Ativo' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editUsuario(row)">Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delusuario(row)">Deletar</button>'  }		
		],

		data: [ 
			{ 'idusuario': "", 'nome': '', 'ativo': 0  }
		]

	}; 			

	$scope.gridOptions.onRegisterApi = function(gridApi){
		$scope.gridApi = gridApi;
	};

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

	$scope.novo = function() {
		$scope.usuario = { 'idusuario': undefined, 'nome': undefined, 'senha': undefined, 'ativo': 0 };
		//console.log($scope.usuario)
	};

	$scope.gravar = function(usuario) {

		//console.log(usuario);

		$scope.param = angular.toJson(usuario);

		console.log($scope.param);

		if (usuario == undefined){
			$scope.novo();
			$scope.getUsuarios();
		}

		if (usuario.idusuario == undefined){

			console.log('POST')

			usuario.idusuario = 0;

			console.log($scope.param)

			$http({
				method: 	"POST",
				url: 		$scope.http + "/usuarios/0",
				data: 		$scope.param,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				$scope.novo();
				$scope.getUsuarios();
			}, function(error){
				console.log("Error... = " + error.status);
			});

		} else {

			console.log('PUT')
			console.log($scope.param)

			$http({
				method: 	"PUT",
				url: 		$scope.http + "/usuarios/0",
				data: 		$scope.param,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				$scope.novo();
				$scope.getUsuarios();
			}, function(error){
				console.log("Error... = " + error.status);
			});
		
		}

	};

//id="input1/(\w+)/\u\1/g" 

	$scope.getUsuarios = function() {
		$http({
			method: 	"GET",
			url: 		$scope.http + "/usuarios/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadusuarios;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editUsuario = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.http + "/usuarios/" + row.entity.idusuario,
			headers: {
				'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.usuario = response.data.cadusuarios[0];
			console.log($scope.usuario)
		}, function(error){
			console.log("Error... = " + error);
		});
	};

	$scope.delusuario = function(row){
		$http({
			method: 	"DELETE",
			url: 		$scope.http + "/usuarios/" + row.entity.idusuario,
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		}).then(function(response){
			$scope.novo();
			$scope.getUsuarios();
		}, function(error){
			console.log("Error = " + error.status);
		});
	};

	$scope.getUsuarios();

});

// http://stackoverflow.com/questions/35254742/tornado-server-enable-cors-requests
