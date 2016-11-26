var app = angular.module('appParametro', ['ui.grid','ngMask','Config']);

app.controller('ctlParametro', function($scope, $http, $location, $window, config) {

	$scope.http = config.link;
	$scope.versao = config.versao;

	$scope.parametro = { 
		'idparam': undefined, 
		'mes':  undefined,
		'ano': undefined, 
		'idempresa': undefined,
		'diasuteis': undefined
	};

    $scope.nomemes = {
        Janeiro : "Janeiro",
        Fevereiro : "Fevereiro",
        Março : "Março",
        Abril : "Abril",
        Maio : "Maio",
        Junho : "Junho",
        Julho : "Julho",
        Agosto : "Agosto",
        Setembro : "Setembro",
        Outubro : "Outubro",
        Novembro : "Novembro",
        Dezembro : "Dezembro"
    };

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idparam', enableCellEdit: false, minWidth: 50, width: 80, displayName: 'Codigo' },
			{ field: 'mes', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Mes' },
			{ field: 'ano', enableCellEdit: false, minWidth: 120, width: 300, displayName: 'Ano' },
			{ field: 'idempresa', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Empresa' },
			{ field: 'diasuteis', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Dias Uteis' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editregistro(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delregistro(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idparam': 0, 'mes': 0, 'ano': 0, 'idempresa': 0, 'diasuteis': 0 }
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
		$scope.parametro = { 
		'idparam': undefined, 
		'mes':  undefined,
		'ano': undefined, 
		'idempresa': undefined,
		'diasuteis': undefined
		};
	};

	$scope.gravar = function(parametro) {

		$scope.parametro = angular.toJson(parametro);

		if (parametro.mes == undefined){
			$scope.novo();
			$scope.getregistro();
		}else{

			if (parametro.idparam == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.http + "/parametro/0",
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
					url: 		$scope.http + "/parametro/0",
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
			url: 		$scope.http + "/parametro/0",
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
			url: 		$scope.http + "/parametro/" + row.entity.idparam,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.parametro = response.data.cadparam[0];
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
				url: 		$scope.http + "/parametro/" + row.entity.idparam,
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

});
