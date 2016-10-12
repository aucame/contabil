
var app = angular.module('appUsuarios', ['ui.grid']);

app.controller('ctlUsuarios', function($scope, $http) {

//17520520

	//$scope.http = "http://200.98.174.103:8080";
	$scope.http = "http://127.0.0.1:8080";

	$scope.gridOptions = {
		enableSorting: false,
		showGridFooter: true,
		enableRowSelection: true,
		enableSelectAll: false,
		enableColumnResizing: true,
		//enableCellEditOnFocus: true,

		columnDefs: [
			{ field: 'idusuarios', enableCellEdit: false, minWidth: 50, width: 90, displayName: 'Codigo' },
			{ field: 'nome', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Nome' },
			{ field: 'ativo', enableCellEdit: false, minWidth: 120, width: 250, displayName: 'Ativo' },
			{ name: 'Editar/Deletar', enableCellEdit: false, width: 200,
			cellTemplate:'<button class="btn btn-primary" ng-click="grid.appScope.editcliente(row)">Editar</button>  <button class="btn btn-primary" ng-click="grid.appScope.delcliente(row)">Deletar</button>'  }		
		],

		data: [ 
			{ 'idusuarios': "" }
		]

	}; 			

	$scope.gridOptions.onRegisterApi = function(gridApi){
		$scope.gridApi = gridApi;
	};

	$scope.novo = function() {
		$scope.cliente = { 'codigo': undefined };
	};

	$scope.gravar = function(cliente) {

		if (cliente == undefined){
			$scope.novo();
			$scope.getcliente();
		}

		if (cliente.codigo == undefined){
			//$http.post("http://localhost:8080/addcliente", $scope.cliente)
			$http(
				{
					method: 	"post",
					url: 		"http://localhost:8080/addcliente",
					data: 		$scope.cliente,
					headers: {
						'Content-Type': 'application/json' 
					}		
				})
			.then(function(data,status,headers,config){
				$scope.novo();
				$scope.getcliente();
			});
		} else {
//				$http.post("insert.php?action=upd_cliente", $scope.cliente)
			$http({
					method: 	"post",
					url: 		"http://localhost:8080/updcliente",
					data: 		$scope.cliente,
					headers: {
						'Content-Type': 'application/json' 
					}	
			}).then(function(data,status,headers,config){
				$scope.novo();
				$scope.getcliente();					
			});				
		}
	};

//id="input1/(\w+)/\u\1/g" 

	$scope.getusuarios = function() {
		$http({
			method: 	"GET",
			url: 		$scope.http + "/usuarios/0",
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		}).then(function(response){
			$scope.gridOptions.data = response.data.cadusuarios;
		}, function(error){
			console.log("Error = " + error);
		});
	};

	$scope.editcliente = function(row){

		var id = row.entity.codigo;

//			$http.post('insert.php?action=edit_cliente', { "id" : id }
		$http.get('http://localhost:8080/getcliente/' + id
		).then(function(response){

			$scope.posts = response.data;

			$scope.cliente = {
				'codigo': 	$scope.posts[0]['codigo'],
				'nome': 	$scope.posts[0]['nome'],
				'endereco': $scope.posts[0]['endereco'],
				'cidade': 	$scope.posts[0]['cidade'],
				'cep': 		$scope.posts[0]['cep']
			};

		}, function(error){
			console.log("Error = " + error);
		});

	};

	$scope.delcliente = function(row){
		var id = row.entity.codigo;
//			$http.post('insert.php?action=del_cliente', { "id" : id }
//			$http.post('http://localhost:8080/delcliente/' + id
		$http({
			method: 	"delete",
			url: 		"http://localhost:8080/delcliente/" + id,
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			}
		}).then(function(response){
			$scope.novo();
			$scope.getcliente();
		}, function(error){
			console.log("Error = " + error);
		});

	};

	$scope.getusuarios();

});

// http://stackoverflow.com/questions/35254742/tornado-server-enable-cors-requests
