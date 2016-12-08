var app = angular.module('appEmpresa', ['ui.grid','ngMask','Config']);

app.controller('ctlEmpresa', function($scope, $http, $location, $window, config) {

	$scope.linkapi = config.linkapi;
	$scope.versao = config.versao;
	$scope.linksite = config.linksite;

	$scope.empresa = { 
		'idempresa': undefined, 
		'nome':  undefined,
		'endereco': undefined, 
		'fonecomercial': undefined
	};

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idempresa', enableCellEdit: false, minWidth: 50, width: 80, displayName: 'Codigo' },
			{ field: 'nome', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Nome' },
			{ field: 'endereco', enableCellEdit: false, minWidth: 120, width: 300, displayName: 'Endereco' },
			{ field: 'fonecomercial', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Fone Comercial' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editregistro(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delregistro(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idempresa': 0, 'nome': '', 'endereco': '', 'fonecomercial': '' }
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
		$scope.empresa = { 
		'idempresa': undefined, 
		'nome':  '',
		'endereco': '', 
		'fonecomercial': ''
		};
	};

	$scope.gravar = function(empresa) {

		$scope.param = angular.toJson(empresa);

		if (empresa.nome == undefined){
			$scope.novo();
			$scope.getregistro();
		}else{

			if (empresa.idempresa == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.linkapi + "/empresas/0",
					data: 		$scope.param,
					headers: {
					'Content-Type': 'application/json'
					}
				}).then(function(response){
					$scope.novo();
					$scope.getregistro();
				}, function(error){
					console.log("Error... = " + error.status);
				});

			} else {
				$http({
					method: 	"PUT",
					url: 		$scope.linkapi + "/empresas/0",
					data: 		$scope.param,
					headers: {
					'Content-Type': 'application/json'
					}
				}).then(function(response){
					$scope.novo();
					$scope.getregistro();
				}, function(error){
					console.log("Error... = " + error.status);
				});
			}
		}
	};

	$scope.getregistro = function() {
		$http({
			method: 	"GET",
			url: 		$scope.linkapi + "/empresas/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadempresa;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editregistro = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.linkapi + "/empresas/" + row.entity.idempresa,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.empresa = response.data.cadempresa[0];
		}, function(error){
			console.log("Error... = " + error);
		});
	};

	$scope.delregistro = function(row){

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
				url: 		$scope.linkapi + "/empresas/" + row.entity.idempresa,
				headers: {
				'Content-Type': 'application/json'
				}
			}).then(function(response){
				$scope.novo();
				$scope.getregistro();
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

	$scope.getregistro();

	$('#nome').focus();

});
