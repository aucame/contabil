$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

var app = angular.module('appCliente', ['ui.grid']);

app.controller('ctlCliente', function($scope, $http, $location) {

	//$scope.http = "http://200.98.174.103:8080";
	$scope.http = "http://127.0.0.1:8080";

	$scope.cliente = { 
		'idcliente': undefined, 
		'nome':  undefined,
		'endereco': undefined, 
		'fonecomercial': undefined,
		'foneresidencial': undefined
	};

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idcliente', enableCellEdit: false, minWidth: 50, width: 80, displayName: 'Codigo' },
			{ field: 'nome', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Nome' },
			{ field: 'endereco', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Endereco' },
			{ field: 'fonecomercial', enableCellEdit: false, minWidth: 120, width: 200, displayName: 'Fone Comercial' },
			{ field: 'foneresidencial', enableCellEdit: false, minWidth: 120, width: 200, displayName: 'Fone Residencial' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editcliente(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delcliente(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idcliente': 0, 'nome': '', 'endereco': '', 'fonecomercial': '', 'foneresidencial': '' }
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
		$scope.cliente = { 
		'idcliente': undefined, 
		'nome':  '',
		'endereco': '', 
		'fonecomercial': '',
		'foneresidencial': ''
		};
	};

	$scope.gravar = function(usuario) {
		$scope.param = angular.toJson(cliente);
		if (cliente.nome == undefined){
			$scope.novo();
			$scope.getcliente();
		}else{

			if (usuario.idcliente == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.http + "/cliente/0",
					data: 		$scope.param,
					headers: {
					'Content-Type': 'application/json'
					}
				}).then(function(response){
					$scope.novo();
					$scope.getcliente();
				}, function(error){
					console.log("Error... = " + error.status);
				});

			} else {
				$http({
					method: 	"PUT",
					url: 		$scope.http + "/cliente/0",
					data: 		$scope.param,
					headers: {
					'Content-Type': 'application/json'
					}
				}).then(function(response){
					$scope.novo();
					$scope.getcliente();
				}, function(error){
					console.log("Error... = " + error.status);
				});
			}
		}
	};

//id="input1/(\w+)/\u\1/g" 

	$scope.getcliente = function() {
		$http({
			method: 	"GET",
			url: 		$scope.http + "/cliente/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadcliente;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editcliente = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.http + "/cliente/" + row.entity.idcliente,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.cliente = response.data.cadcliente[0];
		}, function(error){
			console.log("Error... = " + error);
		});
	};

	$scope.delcliente = function(row){

		swal({
			title: "",
			text: "Deleta o registro ?",
			type: "warning",
			showCancelButton: true,
			confirmButtonColor: "#DD6B55",
			confirmButtonText: "Sim",
			cancelButtonText: "Não",
			closeOnConfirm: false
		},
		function(){

			$http({
				method: 	"DELETE",
				url: 		$scope.http + "/cliente/" + row.entity.idcliente,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				$scope.novo();
				$scope.getcliente();
			}, function(error){
				console.log("Error = " + error.status);
			});

			swal({title: "", text: "Registro deletado com sucesso.", type: "success"});
		});

	};

	$scope.getcliente();

});
