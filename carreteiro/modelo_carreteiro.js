/**
 * Controller principal da App
 * @author Eduardo Hattori
 * @date   2015-11-12
 */
'use strict';
angular.module("CarreteiroApp")
	.controller("mainCtrl",
		["DTOptionsBuilder", "DTColumnBuilder", "carreteiroService", "pedidoService", "romaneioService", "$scope", "$filter", "$location", "$timeout", "SweetAlert", "$rootScope", "$auth", "$q","$compile",
			function(DTOptionsBuilder, DTColumnBuilder, carreteiroService, pedidoService, romaneioService, $scope, $filter, $location, $timeout, SweetAlert, $rootScope, $auth, $q, $compile){
	$scope.loading = true;
	$scope.show = true;
	$scope.carreteirosOriginais = new Array();

	var CarregarCarreteirosExternos = function() {
		carreteiroService.buscarCarreteirosExternos($rootScope.user.filial)
			.success(function(data){
				$scope.carreteirosExternos = data;
			}).error(function(err){
			SweetAlert.error("Erro ao buscar carreteiros", err.message);
		});
	};

	var CarregarEntregas = function(){
		if ($rootScope.user.admin) {
			pedidoService.buscarPedidosFiliais($rootScope.user.filiais).success(function(data){
				$scope.entregas = data;
				$scope.loading = false;
			}).error(function(err){
				SweetAlert.error("Erro ao carregar entregas", err.message);
				$scope.loading = false;
			});
		}
	};

	$scope.CarreteiroOk = function(carreteiro) {
		var entregas = $filter('filter')(carreteiro.romaneios, {entregas:{status: false}});
		return entregas != null ? entregas.length : 0;
	};

	$scope.quantidadeDeEntregasErradasDoRomaneio = function(romaneio) {
		var entregas = $filter('filter')(romaneio.entregas, {status: false});
		return entregas != null ? entregas.length : 0;
	};

	$scope.quantidadeDeEntregasNaoConfirmadasDoRomaneio = function(romaneio) {
		var entregas = $filter('filter')(romaneio.entregas, {entregue: false});
		return entregas != null ? entregas.length : 0;
	};

	$scope.PedidoEntregue = function(numPedVen) {
		var carreteiroDoPedido = null, carreteiroDoPedidoSemRomaneio = null;
		var entregas = 0;
		if ($scope.carreteiros) {
			if ($scope.carreteiros.length > 0) {
				// Romaneio
				carreteiroDoPedido = $filter('filter')($scope.carreteiros, {romaneios:{entregas:{pedido: numPedVen}}});
				if (carreteiroDoPedido != null && typeof(carreteiroDoPedido) != 'undefined') {
					carreteiroDoPedido.forEach(function(carreteiro){
						carreteiro.romaneios.forEach(function(romaneio){
							romaneio.entregas.forEach(function(entrega){
								if (entrega.pedido == numPedVen && entrega.entregue) {
									entregas++;
								}
							});
						});
					});
				}
				// Sem Romaneio
				carreteiroDoPedidoSemRomaneio = $filter('filter')($scope.carreteiros, {entregasSemRomaneio:{pedido: numPedVen}});
				if (carreteiroDoPedidoSemRomaneio != null && typeof(carreteiroDoPedidoSemRomaneio) != 'undefined') {
					carreteiroDoPedidoSemRomaneio.forEach(function(carreteiro){
						carreteiro.entregasSemRomaneio.forEach(function(entrega){
							if (entrega.pedido == numPedVen) {
								entregas++;
							}
						});
					});
				}
			}
		}
		return entregas != null ? entregas : 0;
	};

	$scope.ValorTotalDoRomaneio = function(romaneio) {
		return romaneio.entregas.Sum("valor");
	};

	$scope.valorTotalDasNfsDosRomaneiosDoAba = function(aba) {
		return aba.romaneiosGemco.Sum("valorNf");
	};

	$scope.removerRomaneio = function(carreteiro, romaneio) {
		SweetAlert.confirmApagar("romaneio do carreteiro " + carreteiro.nome, function(){
            var index = carreteiro.romaneios.indexOf(romaneio);
            carreteiro.romaneios.splice(index, 1);
			carreteiroService.removerRomaneio(carreteiro._id, romaneio._id)
				.success(function(data){
					SweetAlert.success("Ok!", "Carreteiro atualizado com sucesso");
                    $location.path('/');
                    carreteiroService.buscarCarreteiroFiliais($rootScope.user.filiais).success(function(data){
                        $scope.carreteirosOriginais.carreteiros = angular.copy(data);
                        $scope.filtro.realizaBusca();
                    });
				})
				.error(function(err){
					SweetAlert.error("Erro ao atualizar carreteiro", err.message);
				});
		}, false);
	};

	$scope.RemoverEntrega = function(carreteiro, entrega) {
		SweetAlert.confirmApagar("entrega do carreteiro " + carreteiro.nome, function(){
			var index = carreteiro.entregas.indexOf(entrega);
			carreteiro.entregas.splice(index, 1);
			carreteiroService.atualizarCarreteiro(carreteiro)
				.success(function(){
					SweetAlert.success("Ok!", "Entrega do carreteiro excluida com sucesso");
					$location.path('/');
				})
				.error(function(err){
					SweetAlert.error("Erro ao atualizar carreteiro", err.message);
				});
		}, false);
	};

	$scope.printRomaneio = function(romaneio, carreteiro){

		carreteiroService.setRomaneioPrint(romaneio);
		carreteiroService.setCarreteiroPrint(carreteiro);
		$timeout(function() {
			$location.path('/romaneio-print');
		});
	};

	$scope.PrintRelatorioGeral = function(){
		carreteiroService.setCarreteirosRelatorioGeral($scope.carreteiros);
		$timeout(function() {
			$location.path('/relatorio-geral/print');
		});
	};

	$scope.printEntregasConfirmadas = function(id) {
		var carreteiro = $scope.carreteiros[$scope.carreteiros.indexOfObject("_id", id)];
		carreteiroService.setCarreteiroPrint(carreteiro);
		$timeout(function() {
			$location.path('/fechamento/print');
		});
	}

	$scope.editarRomaneio = function(romaneio, carreteiro){

        carreteiroService.setRomaneioPrint(romaneio);
		carreteiroService.setCarreteiroPrint(carreteiro);
		$timeout(function() {
			$location.path('/romaneio/edit');
		});
	};

	var ExisteCarreteiros = function() {
		$scope.show = ($scope.carreteiros) ? $scope.carreteiros.length > 0 : false;
	};

	$scope.tipoEntrega = function(tipoEntrega) {
		return carreteiroService.tipoEntrega(tipoEntrega);
	};

	if($auth.isAuthenticated()) {
		//TO-DO: melhorar fluxo de carregamento

		var token = $auth.getToken();
		var base64Url = token.split('.')[1];
		var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

		var user = JSON.parse(decodeURIComponent(escape(window.atob(base64))));
		$rootScope.user = user;

		loadGrid();

	} else{
		$location.path("/login");
	}

  /***
   * Métodos responsáveis pelo filtros da tela
   * de Carreteiros
   *
   * @author: Eduardo Hattori
   * @data: 25/02/2016
   *
   */

  /**
   * Objeto que define os campos dos filtros
   * @type {{dataInicial: null, dataFinal: null, Status: string, Filiais: Array, Carreteiros: Array}}
   */
  $scope.filtro = {

      /**
       * Com este filtro a pesquisa busca todos os
       * registros que sua data seja maior ou igual
       * a dataInial
       */
      dataInicial: null,
      /**
       *
       * Com este filtro a pesquisa busca todos os
       * registros que sua data seja menor ou igual
       * a dataIFinal
       */
      dataFinal  : null,

      /**
       * Com este filtro a pesquisa busca todos os
       * registros que seu Status for true | false
       * Ou registros com qualquer Status 'Todos'
       */
      Status 	   : "Todos",

      /**
       * Com este filtro a pesquisa busca todos os
       * registros pertencerem as filiais listadas
       * no campo Filiais
       */
      Filiais      : new Array(),

      /**
       * Com este filtro a pesquisa busca todos os
       * registros pertencerem aos carreteiros listados
       * no campo Carreteiros
       */
      Carreteiros   : new Array(),

      /**
       * Propriedadde que define se o filtro vai ser exibido
       */
      mostrarFiltro  : false,

     /***
      * Padrão ja vem selecionados todos os carreteiros
      */
      TodosCarreteiros : true,

      /***
       * Padrão ja vem selecionados todas as filiais do usuário
       */
      TodasFiliais : true,

      /***
       * Função responsável por adicionar uma filial
       * a ser filtrada
       *
       * @param filial
       */
      addFilial      : function(filial){
          if(this.Filiais.indexOf(filial) == -1){
              this.Filiais.push(filial);
          }
      },

     /***
      * Adiciona um carreteiro Único
      * @param carreteiro
      */
      addCarreteiro  : function(carreteiro){
          if(this.Carreteiros.indexOf(carreteiro) == -1){
              this.Carreteiros.push(carreteiro);
          }
      },

      /**
       * Remove a filial da lista de filtros
       * @param filial
       */
      removeFilial   :   function(filial){

          var pos = this.Filiais.indexOf(filial);

          if(pos > -1)
              this.Filiais.splice(this.Filiais.indexOf(filial),1);
      },

      /**
       * Remove o carreteiro da lista de filtros
       * @param carreteiro
       */
      removeCarreteiro   :   function(carreteiro){

          var pos = this.Carreteiros.indexOf(carreteiro);

          if(pos > -1)
              this.Carreteiros.splice(this.Carreteiros.indexOf(carreteiro),1);
      },

      /**
       * valida se a filial existe no filtro
       * @param filial
       */
      hasFilial : function(filial){
          return  this.Filiais.indexOf(filial);
      },

      /**
       * valida se tem carreteiro
       * @param filial
       */
      hasCarreteiro : function(carreteiro){
          return  this.Carreteiros.indexOf(carreteiro);
      },

      /**
       * Entregas depois de filtradas
       * Campo utilizado para exibição da pagina de
       * impressão do relatório
       *
       */
      EntregasFiltradas : new Array(),


      /**
       * Função q reseta os filtros de pesquisa
       */
      limpar : function(){
          $scope.selecionaTodasFiliais(true);
          $scope.selecionaTodosCarreteiros(true);

          this.dataInicial = null;
          this.dataFinal   = null;
					this.dataInicialRomaneio = null;
          this.dataFinalRomaneio   = null;
          this.Status      = "Todos";

          this.realizaBusca();
      },

      /**
       * Filtra as entragas dos carreteiros
       */
      realizaBusca  : function(){

          /**
           * Realiza o filtro por carreteiros
           */
          $scope.carreteiros = $scope.carreteirosOriginais.carreteiros.filter(function(obj){
              if($scope.filtro.hasCarreteiro(obj.nome) == -1){
                  return false;
              } else {
                  return true;
              }
          });

          /***
          * Valida se a filial do carreteiro vai retornar o resultado
          * Caso não tenha q retora ele remove o carreteiro some com
          * a lista de carreteiro
          */
          var aCarreteiroDeletavel = new Array();
          for(var i = 0; i < $scope.carreteiros.length; i++){
              var pos = $scope.filtro.hasFilial($scope.carreteiros[i].filial);

              if(pos == -1){
                  $scope.filtro.removeCarreteiro($scope.carreteiros[i].nome);
                  aCarreteiroDeletavel.push($scope.carreteiros[i].nome);
              }
          }
          $scope.carreteiros = $scope.carreteiros.filter(function(obj){
              var pos = aCarreteiroDeletavel.indexOf(obj.nome);

              if(pos != -1){
                  return false;
              } else {
                  return true;
              }
          });

          /**
           * Valida se estão todos os carreteiros selecionados ou não
           */
          if($scope.filtro.Carreteiros.length == $scope.carreteirosOriginais.carreteiros.length){
              $scope.filtro.TodosCarreteiros = true;
          } else {
              $scope.filtro.TodosCarreteiros = false;
          }

          /**
           * Valida se estão todas as filiais estão selecionados ou não
           */
          if($scope.filtro.Filiais.length == $scope.user.filiais.length){
              $scope.filtro.TodasFiliais = true;
          } else {
              $scope.filtro.TodasFiliais = false;
          }

         /***
          * Valida as Entregas que estão dentro do periodo informado
          * nas datas dataInicial e dataFinal
          *
          * Valida se as entregas estão de acordo com o Status informado
          * 'Todos' - Todas as entregas independe do Status
          * 'true'  - Somente as Entregas com o true
          * 'false' - Somente as Entregas com false
          *
          */
          var reg = /(\d{2})\/(\d{2})\/(\d{4})/;

          var dtInicial = $scope.filtro.dataInicial ? new Date($scope.filtro.dataInicial.replace(reg, '$3/$2/$1')) : null;
          var dtFinal   = $scope.filtro.dataFinal ? new Date($scope.filtro.dataFinal.replace(reg, '$3/$2/$1')) : null;
					var dtInicialRomaneio = $scope.filtro.dataInicialRomaneio ? new Date($scope.filtro.dataInicialRomaneio.replace(reg, '$3/$2/$1')) : null;
          var dtFinalRomaneio   = $scope.filtro.dataFinalRomaneio ? new Date($scope.filtro.dataFinalRomaneio.replace(reg, '$3/$2/$1')) : null;
          var status    = $scope.filtro.Status != "Todos" ? $scope.filtro.Status : null;
					var dtObj;
					var isValido;

          for(var i = 0; i < $scope.carreteiros.length; i++){

              /**
               * Zera a busca buscando do carreteiro original
               */
              for(var y = 0;y < $scope.carreteirosOriginais.carreteiros.length; y++){
                  if($scope.carreteiros[i]._id == $scope.carreteirosOriginais.carreteiros[y]._id){
                      $scope.carreteiros[i] = angular.copy($scope.carreteirosOriginais.carreteiros[y]);
                  }
              }

							/**
               * Realiza a filtragem dos romaneios
               */
							$scope.carreteiros[i].romaneios = $scope.carreteiros[i].romaneios.filter(function(romaneio){
								var dtObj = new Date(romaneio.data);
								var isValido = true;

								if(dtInicialRomaneio != null && dtObj < dtInicialRomaneio){
										isValido = false;
								}
								if(dtFinalRomaneio != null && dtObj > dtFinalRomaneio){
										isValido = false;
								}
								return isValido;
							});

              /**
               * Realiza a filtragem das datas de entrega dentro dos romaneios
               */
							for(var indexRomaneio = 0; indexRomaneio < $scope.carreteiros[i].romaneios.length; indexRomaneio++){
								if ($scope.carreteiros[i].romaneios[indexRomaneio] != null) {
									$scope.carreteiros[i].romaneios[indexRomaneio].entregas = $scope.carreteiros[i].romaneios[indexRomaneio].entregas.filter(function(obj){
	                  var dtObj = new Date(obj.data);
	                  var isValido = true;

	                  if(dtInicial != null && dtObj < dtInicial){
	                      isValido = false;
	                  }

	                  if(dtFinal != null && dtObj > dtFinal){
	                      isValido = false;
	                  }

	                  if(status != null && obj.status.toString().toLowerCase() != status.toLowerCase()){
	                      isValido = false;
	                  }

	                  return isValido;
		              });
								}
							}

							/**
               * Realiza a filtragem das datas de entrega dentro dos romaneios
               */
							if ($scope.carreteiros[i].entregasSemRomaneio) {
								$scope.carreteiros[i].entregasSemRomaneio = $scope.carreteiros[i].entregasSemRomaneio.filter(function(entregaSemRomaneio){
                  var dtObj = new Date(entregaSemRomaneio.data);
                  var isValido = true;

                  if(dtInicial != null && dtObj < dtInicial){
                      isValido = false;
                  }

                  if(dtFinal != null && dtObj > dtFinal){
                      isValido = false;
                  }

                  if(status != null && entregaSemRomaneio.status.toString().toLowerCase() != status.toLowerCase()){
                      isValido = false;
                  }

                  return isValido;
	              });
							}

          }
      }
  };

  /***
   * Função que é ativada pelo btn para mudar o valor
   * da propriedade filtro
   */
  $scope.mostrarFiltro = function(){
      $scope.filtro.mostrarFiltro = !$scope.filtro.mostrarFiltro;
  };

  /***
   * Método responsável por chamar a função de adição do filtro
   * ou remoção de registro no filtro
   *
   * @param isMostra
   * @param filial
   * @constructor
   * @return Boolean
   */
  $scope.AddOrRemoveListaFiliaisFiltro = function(filial){

      if(this.filtro.hasFilial(filial) == -1){
          $scope.filtro.addFilial(filial);
      } else {
          $scope.filtro.removeFilial(filial);
      }

      this.filtro.realizaBusca();
  };


  /***
   * Método responsável por chamar a função de adição do filtro
   * ou remoção de registro no filtro
   *
   * @param isMostra
   * @param carreteiro
   * @constructor
   * @return Boolean
   */
  $scope.AddOrRemoveListaCarreteiroFiltro = function(carreteiro){

      if(this.filtro.hasCarreteiro(carreteiro) == -1){
          $scope.filtro.addCarreteiro(carreteiro);
      } else {
          $scope.filtro.removeCarreteiro(carreteiro);
      }

      this.filtro.realizaBusca();
  };

  /***
   * Seleciona todos as filiais do usuário para filiais de filtro
   *
   * @param mostraTodas
   */
  $scope.selecionaTodasFiliais = function(mostraTodas){

      if(mostraTodas == true){
          $scope.filtro.Filiais = angular.copy($scope.user.filiais);
      } else {
          $scope.filtro.Filiais = new Array();
      }

      this.filtro.realizaBusca();
  };

  /***
   * Seleciona todos os carreteiros para os carreteiros do filtro
   *
   * @param mostraTodas
   */
  $scope.selecionaTodosCarreteiros = function(mostraTodas){

      if(mostraTodas == false){
          $scope.filtro.Carreteiros = new Array();
      } else {
          for(var i = 0; i < $scope.carreteirosOriginais.carreteiros.length; i++){
              $scope.filtro.addCarreteiro($scope.carreteirosOriginais.carreteiros[i].nome);
          }
      }

      this.filtro.realizaBusca();
  };

	$scope.romaneioDetalhado = function(id){

		var carreteiro = $scope.carreteiros[$scope.carreteiros.indexOfObject("_id", id)];

		romaneioService.getRomaneioByCarreteiro(carreteiro._id, function(err, data){

			if(err) SweetAlert.error("Erro ao buscar o carreteiro", err.message);
			carreteiro.romaneios = data;

			carreteiroService.setCarreteiroDetalhado(carreteiro);
			$timeout(function() {
				$location.path('/carreteiro-detalhado');
			});
		});

	};


	/***
	 *  Configuracao da Grid
	 */
	function loadGrid(){

		var CarregarCarreteiros = function() {

			var defer = $q.defer();
			carreteiroService.buscarCarreteiroFiliais($rootScope.user.filiais)
				.then(function(result){

					var data = result.data;

					$scope.filtro.Filiais = angular.copy($scope.user.filiais);
					$scope.show = Array.isArray(data) && data.length > 0;

					$scope.carreteiros = data;
					carreteiroService.setCarreteirosCache($scope.carreteiros);
					defer.resolve(data);
			});

			return defer.promise;
		};

		$scope.dtOptions =  DTOptionsBuilder.fromFnPromise(CarregarCarreteiros).withPaginationType('full_numbers').withBootstrap().
			withLanguage({
				sEmptyTable: "Nenhum registro encontrado",
				sInfo: "Mostrando de _START_ até _END_ de _TOTAL_ registros",
				sInfoEmpty: "Mostrando 0 até 0 de 0 registros",
				sInfoFiltered: "(Filtrados de _MAX_ registros)",
				sInfoPostFix: "",
				sInfoThousands: ".",
				sLengthMenu: "_MENU_ resultados por página",
				sLoadingRecords: "Carregando...",
				sProcessing: "Processando...",
				sZeroRecords: "Nenhum registro encontrado",
				sSearch: "Pesquisar: ",
				oPaginate: {
					sNext: "Próximo",
					sPrevious: "Anterior",
					sFirst: "Primeiro",
					sLast: "Último"
				},
				oAria: {
					sSortAscending: ": Ordenar colunas de forma ascendente",
					sSortDescending: ": Ordenar colunas de forma descendente"
				}
			}).withOption('createdRow', function(row) {
				$compile(angular.element(row).contents())($scope);
			})
			//.withOption('aDataSort', false)
			//.withOption('bSort', false)
			.withButtons([
				{
					text: 'Imprimir',
					extend: 'print',
					className: 'btn btn-primary'
				}, {
					text: 'CSV',
					extend: 'csv',
					className: 'btn btn-primary ',
					extension: '.csv'
				}
			]);

		$scope.dtColumns = [
			DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-credit-card-alt"></i> Documento').renderWith(function(data){
				if(data.cnpj || data.cpf)
					return data.cnpj ? '<span>' + cnpj(data.cnpj) + '</span>' : '<span>' + cpf(data.cpf) + '</span>';
				else
					return "";
			}),
			DTColumnBuilder.newColumn('nome').withTitle('<i class="fa fa-truck"></i> Nome'),
			DTColumnBuilder.newColumn('filial').withTitle('<i class="fa fa-home"></i> Filial'),
			DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-file-text"></i> Qtd. Romaneios').renderWith(function(data, type, full, meta) {
				return data.qtdRomaneios ? data.qtdRomaneios : 0;
			}),
			DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-file-text"></i> Qtd. Abastecimento').renderWith(function(data, type, full, meta) {
				return Array.isArray(data.abas) ? data.abas.length : 0;
			}),
			DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-check-circle"></i> Status Entregas').renderWith(function(carreteiro) {
				var qtdEntregas = $scope.CarreteiroOk(carreteiro);
				return qtdEntregas <= 0 ? '<span title="Todas entregas corretas"><i class="fa fa-check-square-o ok"></i></span>' : '<span title="Carreteiro com '+ qtdEntregas +' romaneios(s) com pedido(s) que não era(m) para ser entregue(s)"><i class="fa fa-minus-square erro"> ' + qtdEntregas + '</span>';
			}),
			DTColumnBuilder.newColumn(null).withTitle('Ações').renderWith(function(data){

				var html = '<button type="button" ng-click="romaneioDetalhado(\'' + data._id + '\')" class="btn btn-default"><span title="Detalhar Romaneios" class="fa fa-search"></span></button>';
					html += '<button type="button" ng-click="printEntregasConfirmadas(\'' + data._id + '\')" class="btn btn-primary"><span title="Fechamento" class="fa fa-external-link"></span></button>';

				return '<span  style="white-space: nowrap">'+html+'</span>';
			})
		];

		if(!$scope.user.admin){
			$scope.dtColumns[4].visible = false;
		}

		$scope.dtInstance = {};
	}
	}]);
