var app = angular.module('appUsuarios', ['ui.grid', 'ui.grid.resizeColumns', 'Config']);

app.controller('ctlUsuarios', function($scope, $http, $location, $window, config) {

//17520520

	$scope.linkapi = config.linkapi;
	$scope.versao = config.versao;
	$scope.linksite = config.linksite;

	$scope.usuario = { 
		'idusuario': undefined, 
		'nome':  undefined, 
		'senha': undefined, 
		'ativo': undefined,
		'login': undefined
	};

	$scope.gridOptions = {
		//enableSorting: false,
		//showGridFooter: true,
		//enableRowSelection: true,
		//enableSelectAll: false,
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

	$scope.appMenu = function(menu) {
		if(menu == 'logout'){
			location.href = $scope.linksite;
		} else {
			location.href = $scope.linksite + menu + '.html';
		}
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
					url: 		$scope.linkapi + "/usuarios/0",
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
					url: 		$scope.linkapi + "/usuarios/0",
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
			url: 		$scope.linkapi + "/usuarios/0",
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
			url: 		$scope.linkapi + "/usuarios/" + row.entity.idusuario,
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
				url: 		$scope.linkapi + "/usuarios/" + row.entity.idusuario,
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

	try {
		$scope.login = angular.fromJson($window.sessionStorage.getItem('login'));

		if($scope.login == null){
			$scope.logout();
		};

		} catch(e) {
			console.log('erro');
			$scope.logout();
		};

	$scope.getUsuarios();

	$('#nome').focus();

});
