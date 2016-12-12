
$(function() {
//	$("#valor").maskMoney({prefix:'R$ ', allowNegative: true, thousands:',', decimal:'.', affixesStay: false});
//	$("#valor").maskMoney();
});

var app = angular.module('appLancamento', ['ui.grid','ngMask','Config']);

app.controller('ctlLancamento', function($scope, $http, $location, $window, config) {

	$scope.linkapi = config.linkapi;
	$scope.versao = config.versao;
	$scope.linksite = config.linksite;

	$scope.lancamento = { 
		'idlancamento': undefined, 
		'ano':  undefined,
		'mes': undefined, 
		'idplano': undefined,
		'valor': undefined,
		'idcliente': undefined
	};

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
			{ field: 'idlancamento', enableCellEdit: false, minWidth: 50, width: 100, displayName: 'Numero' },
			{ field: 'idcliente', enableCellEdit: false, minWidth: 50, width: 100, displayName: 'Cliente' },
			{ field: 'ano', enableCellEdit: false, minWidth: 50, width: 100, displayName: 'Ano' },
			{ field: 'mes', enableCellEdit: false, minWidth: 50, width: 100, displayName: 'Mes' },
			{ field: 'idplano', enableCellEdit: false, minWidth: 50, width: 100, displayName: 'Plano' },
			{ field: 'valor', enableCellEdit: false, minWidth: 50, width: 100, displayName: 'Valor' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editregistro(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delregistro(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idlancamento': 0, 'ano': 0, 'mes': undefined, 'idplano': undefined, 'valor': undefined, 'idcliente': undefined }
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
		$scope.lancamento = { 
		'idlancamento': undefined, 
		'ano':  undefined,
		'mes': undefined, 
		'idplano': undefined,
		'valor': undefined,
		'idcliente': undefined
		};
        $scope.selectedOption = $scope.options[0];
	};

	$scope.gravar = function(lancamento) {

		console.log(lancamento.valor);

		$scope.lancamento.mes = $scope.selectedOption.numero;		

		$scope.lancamento = angular.toJson(lancamento);

		if (lancamento.ano == undefined){
			$scope.novo();
			$scope.getregistro();
		}else{

			if (lancamento.idlancamento == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.linkapi + "/lancamentos/0",
					data: 		$scope.lancamento,
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
					url: 		$scope.linkapi + "/lancamentos/0",
					data: 		$scope.lancamento,
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
			url: 		$scope.linkapi + "/lancamentos/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadlancamento;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editregistro = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.linkapi + "/lancamentos/" + row.entity.idlancamento,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.lancamento = response.data.cadlancamento[0];
			mes = response.data.cadlancamento[0].mes;
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
				url: 		$scope.linkapi + "/lancamentos/" + row.entity.idlancamento,
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

	$('#idcliente').focus();

});
