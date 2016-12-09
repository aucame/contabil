angular.module("CarreteiroApp").config(["$routeProvider", "$locationProvider","$httpProvider", "$analyticsProvider", function($routeProvider, $locationProvider, $httpProvider, $analyticsProvider){

  $locationProvider.html5Mode(true);

  $httpProvider.interceptors.push('httpInterceptorFactory');

  $routeProvider.when("/", {
    templateUrl: '/partials/main.html',
    controller: "mainCtrl"
  });

  //$routeProvider.when("/romaneio", {
  //  templateUrl: '/partials/entrega.html',
  //  controller: "entregaCtrl"
  //});

  $routeProvider.when("/romaneio", {
    templateUrl: '/partials/romaneio.html',
    controller: "romaneioCtrl"
  });

  $routeProvider.when("/pagamento/print", {
    templateUrl: '/partials/print.html',
    controller: "printCtrl"
  });

  $routeProvider.when("/romaneio/:edit", {
    templateUrl: '/partials/entrega.html',
    controller: "entregaCtrl"
  });

  $routeProvider.when("/login", {
    templateUrl: '/partials/login.html',
    controller: "loginCtrl"
  });

  $routeProvider.when("/carreteiro", {
    templateUrl: '/partials/carreteiro.html',
    controller: "carreteiroCtrl"
  });

  $routeProvider.when("/usuario-sistema", {
    templateUrl: '/partials/usuarioSistema.html',
    controller: "usuarioSistemaCtrl"
  });

  $routeProvider.when("/relatorio-geral/print", {
    templateUrl: '/partials/printRelatorioGeral.html',
    controller: "relatorioGeralCtrl"
  });

  $routeProvider.when("/romaneio-print", {
    templateUrl: '/partials/printRomaneio.html',
    controller: "printRomaneioCtrl"
  });

  $routeProvider.when("/entregas-confirmadas/print", {
    templateUrl: '/partials/printEntregasConfirmadas.html',
    controller: "printEntregasConfirmadasCtrl"
  });

  $routeProvider.when("/confirmacao-entregas", {
    templateUrl: "/partials/confirmacaoEntrega.html",
    controller: "entregaCtrl"
  });

  $routeProvider.when("/fechamento", {
    templateUrl: "/partials/fechamento.html",
    controller: "fechamentoCtrl"
  });

  $routeProvider.when("/minuta", {
    templateUrl: "/partials/minuta.html",
    controller: "minutaCtrl"
  });

  $routeProvider.when("/carreteiro-detalhado", {
    templateUrl: "/partials/carreteiroDetalhado.html",
    controller: "carreteiroDetalheCtrl"
  });

  $routeProvider.when("/pedido-marcado-para-entregar", {
    templateUrl: "/partials/pedMarcadoEnt.html",
    controller: "pedMarcadoEntCtrl"
  });

  $routeProvider.when("/confirmacao-minuta", {
    templateUrl: "/partials/confirmacaoMinuta.html",
    controller: "confirmacaoMinutaCtrl"
  });

  $routeProvider.when("/acesso-indevido", {
    templateUrl: "/partials/acessoIndevido.html"
  });

  $routeProvider.when("/relatorio-gerencial", {
    templateUrl: "/partials/relatorioGerencial.html",
    controller: "relatorioGerencialCtrl"
  });

  $routeProvider.when("/print-fechamento", {
    templateUrl: "/partials/printFechamento.html",
    controller: "printFechamentoCtrl"
  });
}]);
