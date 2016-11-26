var app = angular.module('appLancamento', ['ui.grid','ngMask','Config']);

app.controller('ctlLancamento', function($scope, $http, $location, $window, config) {

	$scope.http = config.link;
	$scope.versao = config.versao;

	$scope.lancamento = { 
		'idlancamento': undefined, 
		'ano':  undefined,
		'mes': undefined, 
		'idplano': undefined,
		'valor': undefined
	};

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idlancamento', enableCellEdit: false, minWidth: 50, width: 80, displayName: 'Numero' },
			{ field: 'ano', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Ano' },
			{ field: 'mes', enableCellEdit: false, minWidth: 120, width: 300, displayName: 'Mes' },
			{ field: 'idplano', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Plano' },
			{ field: 'valor', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Valor' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editregistro(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delregistro(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idlancamento': 0, 'ano': 0, 'mes': undefined, 'idplano': undefined, 'valor': undefined }
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
		$scope.lancamento = { 
		'idlancamento': undefined, 
		'ano':  undefined,
		'mes': undefined, 
		'idplano': undefined,
		'valor': undefined
		};
	};

	$scope.gravar = function(lancamento) {

		$scope.lancamento = angular.toJson(lancamento);

		if (lancamento.ano == undefined){
			$scope.novo();
			$scope.getregistro();
		}else{

			if (lancamento.idlancamento == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.http + "/lancamentos/0",
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
					url: 		$scope.http + "/lancamentos/0",
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
			url: 		$scope.http + "/lancamentos/0",
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
			url: 		$scope.http + "/lancamentos/" + row.entity.idlancamento,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.lancamento = response.data.cadlancamento[0];
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
				url: 		$scope.http + "/lancamentos/" + row.entity.idlancamento,
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
