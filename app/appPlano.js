var app = angular.module('appPlano', ['ui.grid','ngMask','Config']);

app.controller('ctlPlano', function($scope, $http, $location, $window, config) {

	$scope.http = config.link;
	$scope.versao = config.versao;

	$scope.plano = { 
		'idplano': undefined, 
		'codigo':  undefined,
		'descricao': undefined, 
		'tipocd': undefined
	};

	$scope.debcre = [
		{tipocd: "Selecione", valor: ""},
		{tipocd: "Debito", valor: "D"},
		{tipocd: "Credito", valor: "C"}
	];

    $scope.options = $scope.debcre;
    $scope.selectedOption = $scope.options[0];

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idplano', enableCellEdit: false, minWidth: 50, width: 80, displayName: 'Numero' },
			{ field: 'codigo', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Codigo' },
			{ field: 'descricao', enableCellEdit: false, minWidth: 120, width: 300, displayName: 'Descrição' },
			{ field: 'tipocd', enableCellEdit: false, minWidth: 120, width: 150, displayName: 'Tipo Deb/Cre' },
			{ name: 'Opções', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editregistro(row)"><span class="glyphicon glyphicon-edit"></span> Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delregistro(row)"><span class="glyphicon glyphicon-trash"></span> Deletar</button>'  }		
		],

		data: [ 
			{ 'idplano': 0, 'codigo': 0, 'descricao': undefined, 'tipocd': undefined }
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
		$scope.plano = { 
		'idplano': undefined, 
		'codigo':  undefined,
		'descricao': undefined, 
		'tipocd': undefined
		};
   	    $scope.selectedOption = $scope.options[0];
	};

	$scope.gravar = function(plano) {

		plano.tipocd = $scope.selectedOption.valor;
		$scope.plano = angular.toJson(plano);

		if (plano.codigo == undefined){
			$scope.novo();
			$scope.getregistro();
       	    $scope.selectedOption = $scope.options[0];
		}else{

			if (plano.idplano == undefined){
				$http({
					method: 	"POST",
					url: 		$scope.http + "/planocontas/0",
					data: 		$scope.plano,
					headers: {
					'Content-Type': 'application/json'
					}
				}).then(function(response){
					$scope.novo();
					$scope.getregistro();
            	    $scope.selectedOption = $scope.options[0];
				}, function(error){
					console.log("Error... = " + error.status);
				});

			} else {

				$http({
					method: 	"PUT",
					url: 		$scope.http + "/planocontas/0",
					data: 		$scope.plano,
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
			url: 		$scope.http + "/planocontas/0",
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadplano;
		}, function(error){
			console.log("Error... = " + error.status);
		});
	};

	$scope.editregistro = function(row){
		$http({
			method: 	"GET",
			url: 		$scope.http + "/planocontas/" + row.entity.idplano,
			headers: {
			'Content-Type': 'application/json'
			}
		}).then(function(response){
			$scope.plano = response.data.cadplano[0];
			debcre = response.data.cadplano[0].tipocd;
			if(debcre == "D") {
            	$scope.selectedOption = $scope.options[1];
			} else {
            	$scope.selectedOption = $scope.options[2];
			}
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
				url: 		$scope.http + "/planocontas/" + row.entity.idplano,
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

	$('#codigo').focus();

});
