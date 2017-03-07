var app = angular.module('appParametro', ['ui.grid','ngMask','Config']);

app.controller('ctlParametro', function($scope, $http, $location, $window, config) {

	$scope.linkapi = config.linkapi;
	$scope.versao = config.versao;
	$scope.linksite = config.linksite;

    $scope.meses =	[
					{mes: "Selecione", numero: 00 },
					{mes: "Janeiro", numero: 01 },
        			{mes: "Fevereiro", numero: 02 },
        			{mes: "Março", numero: 03 },
					{mes: "Abril", numero: 04},
					{mes: "Maio", numero: 05},
					{mes: "Junho", numero: 06},
					{mes: "Julho", numero: 07},
					{mes: "Agosto", numero: 08},
					{mes: "Setembro", numero: 09},
					{mes: "Outubro", numero: 10},
					{mes: "Novembro", numero: 11},
					{mes: "Dezembro", numero: 12}
    				];

	$scope.parametro = { 
		'idparam': undefined, 
		'mes':  0,
		'ano': undefined, 
		'idempresa': undefined,
		'diasuteis': undefined,
		'meddiafat': undefined
	};

    $scope.options = $scope.meses;
    $scope.selectedOption = $scope.options[0];

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idparam', enableCellEdit: false, minWidth: 50, width: 150, displayName: 'Codigo' },
			{ field: 'mes', enableCellEdit: false, minWidth: 50, width: 150, displayName: 'Mes' },
			{ field: 'ano', enableCellEdit: false, minWidth: 50, width: 150, displayName: 'Ano' },
			{ field: 'idempresa', enableCellEdit: false, minWidth: 50, width: 150, displayName: 'Empresa' },
			{ field: 'diasuteis', enableCellEdit: false, minWidth: 50, width: 150, displayName: 'Dias Uteis' },
			{ field: 'meddiafat', enableCellEdit: false, minWidth: 50, width: 150, displayName: 'Media Dia Fat.' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editregistro(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delregistro(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idparam': 0, 'mes': 0, 'ano': 0, 'idempresa': 0, 'diasuteis': 0, 'meddiafat': 0 }
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
		$scope.parametro = { 
		'idparam': undefined, 
		'mes':  undefined,
		'ano': undefined, 
		'idempresa': undefined,
		'diasuteis': undefined,
		'meddiafat': undefined
		};
        $scope.selectedOption = $scope.options[0];
	};

	$scope.gravar = function(parametro) {

		$scope.parametro.mes = $scope.selectedOption.numero;		

		$scope.parametro = angular.toJson(parametro);

		if (parametro.mes == undefined){
			$scope.novo();
			$scope.getregistro();
		}else{

			if (parametro.idparam == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.linkapi + "/parametro/0",
					data: 		$scope.parametro,
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
					url: 		$scope.linkapi + "/parametro/0",
					data: 		$scope.parametro,
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
			url: 		$scope.linkapi + "/parametro/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadparam;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editregistro = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.linkapi + "/parametro/" + row.entity.idparam,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.parametro = response.data.cadparam[0];
			mes = response.data.cadparam[0].mes;
            $scope.selectedOption = $scope.options[mes];
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
				url: 		$scope.linkapi + "/parametro/" + row.entity.idparam,
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

	$('#ano').focus();

});
