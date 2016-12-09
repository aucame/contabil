'use strict';
angular.module("CarreteiroApp")
    .controller("carreteiroCtrl", ["AppConfig", "$auth", "carreteiroService", "$scope", "$location", "SweetAlert", "$rootScope", "DTOptionsBuilder", "DTColumnBuilder", "$q", "$compile", "$filter",
        function(appConfig, $auth, carreteiroService, $scope, $location, SweetAlert, $rootScope, DTOptionsBuilder, DTColumnBuilder, $q, $compile, $filter){

            $scope.carreteiro = new Carreteiro();

            $scope.salvarCarreteiro = function (carreteiro) {
                SweetAlert.confirmSalvar("carreteiro", function(){
                    carreteiro.cnpj = carreteiro.cnpj.replace( /\D+/g, '');
                    if (carreteiro.nome !== "" && carreteiro.filial > 0 && $scope.inputPrecoFixo !== "") {

                        if(carreteiro.precos.indexOfObject('descricao', 'fixo') == -1){
                            carreteiro.precos.push({
                                    descricao : 'fixo',
                                    carreteiro_mongo_id : carreteiro._id,
                                    tipo : 'D'
                                });
                        }

                        if(carreteiro.precos.indexOfObject('descricao', 'gris') == -1){
                            carreteiro.precos.push({
                                descricao : 'gris',
                                carreteiro_mongo_id : carreteiro._id,
                                tipo : 'D'
                            });
                        }

                        if(carreteiro.precos.indexOfObject('descricao', 'advalorem') == -1){
                            carreteiro.precos.push({
                                descricao : 'advalorem',
                                carreteiro_mongo_id : carreteiro._id,
                                tipo : 'D'
                            });
                        }

                        if(carreteiro.precos.indexOfObject('descricao', 'pedagioPorEntrega') == -1){
                            carreteiro.precos.push({
                                descricao : 'pedagioPorEntrega',
                                carreteiro_mongo_id : carreteiro._id,
                                tipo : 'D'
                            });
                        }

                        carreteiro.precos.forEach(function(preco){

                            switch (preco.descricao){
                                case 'fixo':
                                    preco.valor = $scope.inputPrecoFixo ? $scope.inputPrecoFixo : 0;
                                    break;
                                case 'gris':
                                    preco.valor = $scope.inputGris ? $scope.inputGris : 0;
                                    break;
                                case 'advalorem':
                                    preco.valor = $scope.inputAdvalorem ? $scope.inputAdvalorem : 0;
                                    break;
                                case 'pedagioPorEntrega':
                                    preco.valor = $scope.inputPedagioPorEntrega ? $scope.inputPedagioPorEntrega : 0;
                                    break;
                            }

                        });

                        if(carreteiro._id){

                            carreteiroService.atualizarCarreteiroCadastro(carreteiro).success(function(data) {
                              buscarCarreteiros().then(function() {
                                $scope.dtInstance.reloadData(function(json){}, true);
                                callbackSucesso;
                              })
                            }).error(callbackErro);
                        } else{
                            carreteiroService.salvarCarreteiro(carreteiro).success(function() {
                              buscarCarreteiros().then(function() {
                                $scope.dtInstance.reloadData(function(json){}, true);
                                callbackSucesso;
                              })
                            }).error(callbackErro);
                        }
                        $scope.limparCarreteiro();
                    }
                });
            };

            $scope.editarCarreteiro = function(carreteiro){
                if(carreteiro){
                    if(carreteiro.hasOwnProperty('cnpj')){
                        carreteiro.cnpj = formataCpfCnpj(carreteiro.cnpj.replace( /\D+/g, ''));
                    }
                    $scope.carreteiro = carreteiro;

                    carreteiro.precos.forEach(function(preco){
                        if(preco.descricao == "fixo")
                            $scope.inputPrecoFixo = preco.valor;
                        if(preco.descricao == "gris")
                            $scope.inputGris = preco.valor;
                        if(preco.descricao == "advalorem")
                            $scope.inputAdvalorem = preco.valor;
                        if(preco.descricao == "pedagioPorEntrega")
                            $scope.inputPedagioPorEntrega = preco.valor;
                    });

                } else {
                    $scope.limparCarreteiro();
                }
            };

            $scope.buscarCarreteiroId = function(id) {

              carreteiroService.buscarCarreteiroId(id).success(function(data) {
                $scope.isEdicaoOuNovo = true;
                $scope.editarCarreteiro(data);
              }).error(function(err){
                  console.log(err);
              });
            },

            $scope.limparCarreteiro = function() {
              $scope.carreteiro = new Carreteiro();
              $scope.placa      = "";
              $scope.motorista  = {};
              $scope.aba        = {};
              $scope.isEdicaoOuNovo = !$scope.isEdicaoOuNovo;
              $scope.inputPrecoFixo           = "";
              $scope.inputGris                = "";
              $scope.inputAdvalorem           = "";
              $scope.inputPedagioPorEntrega   = "";
            };

            $scope.adicionarPrecoAba = function (precoAba) {

                if(!Array.isArray($scope.carreteiro.precos))
                    $scope.carreteiro.precos = new Array();

                if(!$scope.carreteiro.precos.some(function(element){
                        return element.descricao == precoAba.descricao;
                    })){
                    $scope.aba    = {};
                    precoAba.tipo = 'A';
                    precoAba.carreteiro_mongo_id = $scope.carreteiro._id;
                    $scope.carreteiro.precos.push(precoAba);
                    $('#inputDescricaoPreco').focus();
                } else {
                    SweetAlert.warning("Preço já foi inserido.");
                    $scope.aba    = {};
                }
            };

            $scope.removerPrecoAba = function(precoAba){
                var index = $scope.carreteiro.precos.indexOf(precoAba);
                $scope.carreteiro.precos.splice(index, 1);
            };

            $scope.adicionarMotorista = function (motorista) {
                if(!$scope.carreteiro.motoristas.some(function(element){
                        return element.rg == motorista.rg;
                    })){
                    $scope.motorista = {};
                    $scope.carreteiro.motoristas.push(motorista);
                    $('#inputNomeMotorista').focus();
                } else {
                    SweetAlert.warning("Motorista já foi inserido.");
                }
            };

            $scope.removerMotorista = function(motorista){
                var index = $scope.carreteiro.motoristas.indexOf(motorista);
                $scope.carreteiro.motoristas.splice(index, 1);
            };

            $scope.motoristaEnter = function(event, motorista) {
                if (event.keyCode == 13 && motorista.nome && motorista.rg) {
                    $scope.adicionarMotorista(motorista);
                }
            };

            $scope.adicionarPlaca = function (placa) {

                if(!Array.isArray($scope.carreteiro.placas)){
                    $scope.carreteiro.placas = [];
                }

                if(!$scope.carreteiro.placas.some(function(element){
                        return element == placa;
                    })){
                    $scope.placa = "";
                    $scope.carreteiro.placas.push(placa);

                    $('#inputPlacas').focus();
                } else {
                    SweetAlert.warning("Placa já foi inserida.");
                }
            };

            $scope.removerPlaca = function(placa){
                $scope.carreteiro.placas.splice($scope.carreteiro.placas.indexOf(placa), 1);
            };

            $scope.placaEnter = function(event, placa) {
                if (event.keyCode == 13 && placa) {
                    $scope.adicionarPlaca(placa);
                }
            };

            $scope.listaTransportadoras = function(param) {
                return carreteiroService.buscarTransportadora(param);
            };

            $scope.onSelect = function ($item, $model, $label) {

                $scope.carreteiro.nome = $item.name;
                $scope.carreteiro.cnpj = $item.cnpj ? cnpjMask($item.cnpj) : cpfMask($item.cpf);
                $scope.inputPesqTransp = "";

            };

            function buscarCarreteiros(){
                var defer = $q.defer();

                carreteiroService.buscarCarreteiro().success(function(data){
                    $scope.carreteiros = data;

                    if(carreteiroLocation){
                      buscaCarreteiroExistente();
                    }

                    defer.resolve(data);

                }).error(callbackErro);

                return defer.promise;
            };

            function callbackSucesso(){
                SweetAlert.success("Ok!", "Carreteiro salvo com sucesso");
                buscarCarreteiros();
            };

            function callbackErro(err){
                if(err.message){
                    SweetAlert.error("Não foi possível concluir essa ação.", err.message);
                } else {
                    SweetAlert.error("Não foi possível concluir essa ação.", err);
                }
            };

            if($auth.isAuthenticated()) {
                $scope.isEdicaoOuNovo           = false;
                $scope.inputPrecoFixo           = "";
                $scope.inputGris                = "";
                $scope.inputAdvalorem           = "";
                $scope.inputPedagioPorEntrega   = "";

                $rootScope.user = $auth.getPayload();
                var carreteiroLocation = $location.search().id;
                if(carreteiroLocation){
                  $scope.isLoading = true;
                }
                //buscarCarreteiros();
            } else{
                $location.path("/in");
            }

            var buscaCarreteiroExistente = function(){

                 $scope.carreteiros.forEach(function(res) {
                   if(res._id === carreteiroLocation){
                     $scope.editarCarreteiro(res);
                     $scope.isLoading = false;
                   }
                 });
            }

            function cpfMask(input) {

                var str = input + '';
                str = str.replace(/\D/g, '');
                str = str.replace(/(\d{3})(\d)/, '$1.$2');
                str = str.replace(/(\d{3})(\d)/, '$1.$2');
                str = str.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
                return str;

            }

            function cnpjMask(input) {

              var str = input + '';
              str = str.replace(/\D/g, '');
              str = str.replace(/^(\d{2})(\d)/, '$1.$2');
              str = str.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
              str = str.replace(/\.(\d{3})(\d)/, '.$1/$2');
              str = str.replace(/(\d{4})(\d)/, '$1-$2');
              return str;

            }

            function formataCpfCnpj(input) {
              if (input.length <= 11){
                return cpfMask(input);
              } else {
                return cnpjMask(input);
              }
            }

            function criarObjetoPrecos(carreteiro){
                var precos = [];

                if (carreteiro.precos.fixo)
                    precos.push(addObjetoPreco(carreteiro.carreteiro_mongo_id, 'D', carreteiro.precos.fixo, 'fixo'));

                if (carreteiro.precos.gris)
                    precos.push(addObjetoPreco(carreteiro.carreteiro_mongo_id, 'D', carreteiro.precos.gris, 'gris'));;

                if (carreteiro.precos.advalorem)
                    precos.push(addObjetoPreco(carreteiro.carreteiro_mongo_id, 'D', carreteiro.precos.advalorem, 'advalorem'));

                if (carreteiro.precos.pedagioPorEntrega)
                    precos.push(addObjetoPreco(carreteiro.carreteiro_mongo_id, 'D', carreteiro.precos.pedagioPorEntrega, 'pedagioPorEntrega'));

                return precos;
            }

            function addObjetoPreco(carreteiroMongoId, tipo, valor, descricao){
                return { carreteiro_mongo_id : carreteiroMongoId, tipo : tipo, valor : valor, descricao : descricao };
            }

            function montarObjetoPrecosParaTela(carreteiro){
                if (carreteiro.precos){
                    carreteiro.precos.forEach(function(preco){
                        if (preco.descricao == 'fixo') carreteiro.precos.fixo = preco.valor;
                        if (preco.descricao == 'gris') carreteiro.precos.gris = preco.valor;
                        if (preco.descricao == 'advalorem') carreteiro.precos.advalorem = preco.valor;
                        if (preco.descricao == 'pedagioPorEntrega') carreteiro.precos.pedagioPorEntrega = preco.pedagioPorEntrega;
                    });
                }
            }




            $scope.dtOptions =  DTOptionsBuilder.fromFnPromise(buscarCarreteiros).withPaginationType('full_numbers').withBootstrap().
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
        			DTColumnBuilder.newColumn('nome').withTitle('<i class="fa fa-truck"></i> Nome'),
        			DTColumnBuilder.newColumn('filial').withTitle('<i class="fa fa-home"></i> Filial'),
        			DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-usd"></i> Preço Fixo').renderWith(function(data, type, full) {

                        var precoFixo = 0.00;

                        if(data.precos && Array.isArray(data.precos) & data.precos.length > 0){
                            data.precos.forEach(function(preco){
                                if(preco.descricao == 'fixo')
                                    precoFixo = preco.valor;
                            });
                        }

                        return  $filter('currency')(precoFixo);
        			}),
        			DTColumnBuilder.newColumn(null).withTitle('Ações').renderWith(function(data){
                var html = '<button class="btn btn-info btn-xs" ng-click="buscarCarreteiroId(\'' + data._id + '\')"><span class="glyphicon glyphicon-edit"></span></button>';
        				return '<span  style="white-space: nowrap">'+html+'</span>';
        			})
        		];

            $scope.dtInstance = {};

        }]);
