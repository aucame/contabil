var app = angular.module('appCliente', ['ui.grid','ngMask','Config']);

app.controller('ctlCliente', function($scope, $http, $location, $window, config) {

	$scope.linkapi = config.linkapi;
	$scope.versao = config.versao;
	$scope.linksite = config.linksite;

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
			{ field: 'endereco', enableCellEdit: false, minWidth: 120, width: 300, displayName: 'Endereco' },
			{ field: 'fonecomercial', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Fone Comercial' },
			{ field: 'foneresidencial', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Fone Residencial' },
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

	$scope.appMenu = function(menu) {
		if(menu == 'logout'){
			location.href = $scope.linksite;
		} else {
			location.href = $scope.linksite + menu + '.html';
		}
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

	$scope.gravar = function(cliente) {

		$scope.param = angular.toJson(cliente);

		if (cliente.nome == undefined){
			$scope.novo();
			$scope.getcliente();
		}else{

			if (cliente.idcliente == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.linkapi + "/clientes/0",
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
					url: 		$scope.linkapi + "/clientes/0",
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
			url: 		$scope.linkapi + "/clientes/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadclientes;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editcliente = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.linkapi + "/clientes/" + row.entity.idcliente,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.cliente = response.data.cadclientes[0];
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
				url: 		$scope.linkapi + "/clientes/" + row.entity.idcliente,
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

	try {
		$scope.login = angular.fromJson($window.sessionStorage.getItem('login'));

		if($scope.login == null){
			$scope.logout();
		};

		} catch(e) {
			console.log('erro');
			$scope.logout();
		};

	$scope.getcliente();
	
	$('#nome').focus();
	
});
