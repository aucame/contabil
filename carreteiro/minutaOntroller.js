'use strict';
  angular.module("CarreteiroApp")
.controller("minutaCtrl",
["DTOptionsBuilder", "DTColumnBuilder", "carreteiroService", "minutaService", "$scope", "$filter", "$location", "$timeout", "SweetAlert", "$rootScope", "$auth","$q", "$compile",
  function(DTOptionsBuilder, DTColumnBuilder, carreteiroService, minutaService, $scope, $filter, $location, $timeout, SweetAlert, $rootScope, $auth, $q, $compile){

  var dateFormat = "DD/MM/YYYY";
  $scope.exibeAlerta = false;
  $scope.exibeAlertaSelecao = false;
  $scope.exibeGrid = false;
  $scope.isLoading = true;

  function buscarCarreteiro(){

      var filiais = new Array();

      if($scope.filial !== "")
          filiais = [$scope.filial];
      else
        filiais =  $scope.filiais;

      carreteiroService.buscarCarreteiroFiliais(filiais)
          .success(function(data){

              $scope.isLoading = false;
              $scope.carreteiros = data;
              $scope.carreteiroOriginal = angular.copy(data);
          })
          .error(function(err) {
              SweetAlert.error("Erro ao buscar carreteiros", err);
          });
  };

  $scope.buscarMinutaId = function(id){
    minutaService.buscarMinutaId(id).then(function(dados){
     var _data = dados.data.records[0];
     var path = _data.filePath;
     window.open(path);
    });
  };

  $scope.recarregaTransportadores = function(){

      if($scope.filial !== null){
          $scope.carreteiros = new Array();

          $scope.carreteiroOriginal.forEach(function(item){
              if(item.filial == $scope.filial){
                  $scope.carreteiros.push(item);
              }

          });

      } else {
          $scope.carreteiros = $scope.carreteiroOriginal;
      }
  };

  $scope.formataCarreteiro = function(carreteiro){
      return carreteiro.nome + " - " + carreteiro.filial;
  };

  $scope.pesquisarMinutas = function(){

      $scope.exibeAlertaSelecao = false;
      $scope.exibeAlerta = false;

      if ($scope.carreteiro == null)
      {
          document.getElementById("inputIdCarreteiro").focus();
          $scope.exibeAlertaSelecao = true;
          $scope.exibeGrid = false;
      }
      else if($scope.carreteiro){
          if ($scope.cnpj.length <= 11){
              $scope.cnpjformatado = cpf($scope.carreteiro.cnpj);
          }
          else {
              $scope.cnpjformatado = cnpj($scope.carreteiro.cnpj);
          }

          $scope.cnpj = $scope.carreteiro.cnpj.replace(/[^0-9]/g,'');
          $scope.nome = $scope.carreteiro.nome;
          $scope.dtInstance.reloadData(function(json){}, true);

      }
      else {
          $scope.exibeAlerta = false;
      }
  };

  function loadGrid() {

    var carregarMinutas = function(){
      var defer = $q.defer();
      var cnpjcpf = $scope.cnpj;
      var filial = $scope.filial;

      if(cnpjcpf == ""){
          defer.resolve([]);
      } else {
        minutaService.buscarMinutas(cnpjcpf, filial)
          .then(function(retorno){
              var _data = [];

               if(retorno.data.statusCodeAPIGEE){
                 $scope.exibeGrid = false;
                 $scope.exibeAlerta = true;
               }
               else{
                 _data = retorno.data.records;
                 $scope.exibeGrid = true;
                 $scope.exibeAlerta = false;
               }
              defer.resolve(_data);
          });
      }
      return defer.promise;
  };

  $scope.dtOptions =  DTOptionsBuilder.fromFnPromise(carregarMinutas).withPaginationType('full_numbers').withBootstrap().
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
			}).withButtons([
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
      DTColumnBuilder.newColumn(null).withTitle('ID Minuta').renderWith(function(data){
        if (data.status == 1){
            return '<span style=color:red>' + data.id + '</span>';
        } else {
            return data.id;
        }
      }).withOption('sWidth', '10%'),
      DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-calendar"></i> Data Minuta').renderWith(function(data){
        if (data.status == 1){
            return '<span style=color:red>' + moment(data.dispatchDate.toString()).format(dateFormat) + '</span>';
        } else {
            return moment(data.dispatchDate.toString()).format(dateFormat);
        }
      }).withOption('sWidth', '15%'),
      DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-credit-card-alt"></i> CNPJ/CPF').renderWith(function(data){
        if (data.status == 1){
            return data.carrier.cnpj ? '<span style=color:red>' + cnpj(data.carrier.cnpj) + '</span>' : '<span style=color:red>' + cpf(data.carrier.cpf) + '</span>';
        } else {
            return data.carrier.cnpj ? '<span>' + cnpj(data.carrier.cnpj) + '</span>' : '<span>' + cpf(data.carrier.cpf) + '</span>';
        }
			}).withOption('sWidth', '15%'),
      DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-truck"></i> Transportadora').renderWith(function(data){
        if (data.status == 1){
            return '<span style=color:red>' + data.carrier.name + '</span>';
        } else {
            return data.carrier.name;
        }
      }).withOption('sWidth', '34%'),
      DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-bars"></i> Placa').renderWith(function(data){
        if (data.status == 1){
            return '<span style=color:red>' + data.vehicle.licensePlate + '</span>';
        } else {
            return data.vehicle.licensePlate;
        }
      }).withOption('sWidth', '8%'),
      DTColumnBuilder.newColumn(null).withTitle('<i class="fa fa-home"></i> Filial').renderWith(function(data){
        if (data.status == 1){
            return '<span style=color:red>' + data.branch.id + '</span>';
        } else {
            return data.branch.id;
        }
      }).withOption('sWidth', '8%'),
      DTColumnBuilder.newColumn(null).withTitle('Ações').renderWith(function(data){
        var btn;
        btn  = '<button type="button" ng-click="cancelarMinuta(' + data.id + ',' + data.status + ')" class="btn btn-danger btn-xs"><span class="glyphicon glyphicon-remove" title="Cancelar Minuta"></span></button> ';
        btn += '<button type="button" ng-click="buscarMinutaId(' + data.id + ')" class="btn btn-primary btn-xs"><span class="fa fa-print" title="Imprimir Minuta"></span></button> ';
        return btn;
			}).withOption('sWidth', '15%')
		];
    $scope.dtInstance = {};
  };



  $scope.cancelarMinuta = function(minutaId, statusMinuta){
    if (statusMinuta == 1){
        SweetAlert.swal("Operação não permitida!", "Minuta já cancelada!", "error");
    } else {
        SweetAlert.swal({
         html: true,
         title: "Cancelamento Minuta",
         text: "Deseja realmente cancelar a minuta <font color=red><b>" + minutaId + "</b></font>?",
         type: "warning",
         showCancelButton: true,
         cancelButtonText: "Cancelar",
         confirmButtonColor: "#3C763D",confirmButtonText: "Confirmar",
         closeOnConfirm: false,
         closeOnCancel: false },
         function(isConfirm) {
           if (isConfirm) {

             minutaService.cancelarMinuta(minutaId).then(function(dados){
               if (dados.status == 200){

                 SweetAlert.swal({
                   html: true,
                   title: "Sucesso!",
                   type: "success",
                   text: "Minuta <font color=red><b>" + minutaId + "</b></font> cancelada com sucesso!"},
                   function(isConfirm) {
                     if (isConfirm)  $scope.pesquisarMinutas();
                 });

               } else {
                 SweetAlert.swal({
                   html: true,
                   title: "Erro ao cancelar minuta!",
                   type: "error",
                   text: "Minuta <font color=red><b>" + minutaId + "</b></font> "});
               }
             });
           } else {
             SweetAlert.swal({
              html: true,
              type: "info",
              title: "Operação abortada!",
              text: "Minuta <font color=red><b>" + minutaId + "</b></font> não cancelada"});
           }
         });
    }
  };

  if($auth.isAuthenticated()) {
    $rootScope.user = $auth.getPayload();
    $scope.filiais = $rootScope.user.filiais;
    $scope.filiais.sort();
    $scope.filial = "";
    $scope.cnpj = "";
    buscarCarreteiro();
    loadGrid();
  } else{
    $location.path("/login");
  };

}]);
