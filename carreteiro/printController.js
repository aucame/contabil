angular.module("CarreteiroApp").controller("printCtrl",
	["$auth", "carreteiroService", "$scope", "$window", "$location", "$filter", "$rootScope",
		function($auth, carreteiroService, $scope, $window, $location, $filter, $rootScope){

			$scope.carreteiro = carreteiroService.getCarreteiroPrint();
			$scope.print = carreteiroService.getPagamentoPrint();

			$scope.ValorTotalDoPagamento = function(pagamento) {
				return pagamento.canhotos.Sum("valor");
			};

			$scope.PagamentoOk = function(pagamento) {
				var canhotos = $filter('filter')(pagamento.canhotos, {status: false});
				return canhotos != null ? canhotos.length : 0;
			};

			$scope.printPagamento = function(){
				$window.print();
			};

			$scope.voltar = function() {
				$location.path('/');
			};

			if($auth.isAuthenticated()) {
				$rootScope.user = $auth.getPayload();
				$scope.user = data;
			} else{
				$location.path("/login");
			}

		}]);
