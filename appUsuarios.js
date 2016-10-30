$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

var app = angular.module('appUsuarios', ['ui.grid']);

app.controller('ctlUsuarios', function($scope, $http, $location) {

//17520520

	//$scope.http = "http://200.98.174.103:8080";
	$scope.http = "http://127.0.0.1:8080";

	$scope.usuario = { 
		'idusuario': undefined, 
		'nome':  undefined, 
		'senha': undefined, 
		'ativo': undefined,
		'login': undefined
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
			{ field: 'login', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Login' },
			{ field: 'ativo', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Ativo' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editUsuario(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delusuario(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idusuario': 0, 'nome': '', 'login': '', 'ativo': '' }
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
		$scope.usuario = { 
		'idusuario': undefined, 
		'nome':  '', 
		'login': '', 
		'senha': '', 
		'ativo': '' 
		};
	};

	$scope.gravar = function(usuario) {
		$scope.param = angular.toJson(usuario);
		if (usuario.nome == undefined){
			$scope.novo();
			$scope.getUsuarios();
		}else{

			if (usuario.idusuario == undefined){
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
		}, function(error){
			console.log("Error... = " + error);
		});
	};

	$scope.delusuario = function(row){

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
				url: 		$scope.http + "/usuarios/" + row.entity.idusuario,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				$scope.novo();
				$scope.getUsuarios();
			}, function(error){
				console.log("Error = " + error.status);
			});

			swal({title: "", text: "Registro deletado com sucesso.", type: "success"});
		});

	};

	$scope.getUsuarios();

});
