angular.module("CarreteiroApp")
    .factory("carreteiroService", [ "$http","$sce", function($http, $sce){

  var pagamentoPrint = null;
  var carreteiroPrint = null;
  var carreteiros = null;
  var romaneioPrint = null;
  var romaneiosPrint = null;
  var carreteirosCache = null;

  return {

    getLocation: function(param){
      return $http.get('/api/carreteiro/transportadora/' + param);
    },

    salvarCarreteiro: function(carreteiro){
      return $http.post('/api/carreteiro/', carreteiro);
    },

    atualizarCarreteiroCadastro: function(carreteiro){
      return $http.put('/api/carreteiro-cadastro/', carreteiro);
    },

    atualizarCarreteiro: function(carreteiro){
      return $http.put('/api/carreteiro/', carreteiro);
    },

    atualizarConfirmacaoEntrega : function(body){
      return $http.put('/api/carreteiro/confirmacao-entrega/', body);
    },

    buscarCarreteiroFilial: function(filial){
      return $http.get('/api/carreteiro/filial/'+filial);
    },

    buscarCarreteiroFiliais: function(filiais){
      return $http.get('/api/carreteiro/filiais/'+filiais.toString());
    },

    buscarCarreteiro: function(){
      return $http.get('/api/carreteiro/');
    },

    buscarCarreteiroId: function(id){
      return $http.get('/api/carreteiro-id/'+ id);
    },

    buscarCarreteirosExternos: function(filial){
      return $http.get('/api/carreteiro/externos/' + filial);
    },

    setPagamentoPrint: function(pagamento){
      pagamentoPrint = pagamento;
    },

    getPagamentoPrint: function(){
      return pagamentoPrint;
    },

    setCarreteiroPrint: function(carreteiro){
      carreteiroPrint = carreteiro;
    },

    getCarreteiroDetalhado: function(id, callback){
      $http.get('/api/carreteiro-id/' + id).success(function(response){
        callback(null, response);
      });
    },

    setCarreteirosCache : function(aCarreteiros){
      carreteirosCache = aCarreteiros;
    },

    getCarreteirosCache : function(){
        return carreteirosCache;
    },

    getCarreteiroPrint: function(){
      return carreteiroPrint;
    },

    setCarreteirosRelatorioGeral: function(_carreteiros){
      carreteiros = _carreteiros;
    },

    getCarreteirosRelatorioGeral: function(){
      return carreteiros;
    },

    setRomaneioPrint: function(romaneio){
      romaneioPrint = romaneio;
    },

    getRomaneioPrint: function(){
      return romaneioPrint;
    },

    setRomaneiosPrint: function(romaneios){
      romaneiosPrint = romaneios;
    },

    getRomaneiosPrint: function(){
      return romaneiosPrint;
    },

    adicionarRomaneio: function(carreteiro, romaneio){

      var objRomaneio = {
        carreteiro_mongo_id  : carreteiro._id,
        usuario              : romaneio.usuario.toUpperCase(),
        data                 : romaneio.data,
        filial               : carreteiro.filial,
        placa                : romaneio.placa,
        carreteiro_nome      : carreteiro.nome,
        carreteiro_documento : carreteiro.cnpj ? carreteiro.cnpj : carreteiro.cpf,
        motorista_nome       : romaneio.motorista.nome,
        motorista_rg         : romaneio.motorista.rg,
        entregas : []
      };

      romaneio.entregas.forEach(function(entrega){

        objRomaneio.entregas.push({
          data:     new Date(),
          pedido:   entrega.pedido,
          valor:    entrega.valor,
          status:   entrega.status,
          entregue: entrega.entregue,
          filial:   entrega.filial,
          tipo  :   entrega.tipo
        });
      });

      return $http.post('/api/carreteiro/' + objRomaneio.carreteiro_mongo_id + '/romaneio', objRomaneio);

    },

    adicionarPlaca: function(carreteiro, placa){
      return $http.put('/api/carreteiro/placa/', {"carreteiro": carreteiro, "placa": placa});
    },

    adicionarMotorista: function(carreteiro, motorista){
      return $http.put('/api/carreteiro/motorista/', {"carreteiro": carreteiro, "motorista": motorista});
    },

    removerRomaneio: function(carreteiro, romaneio){
      return $http.delete('/api/carreteiro/romaneio/' + carreteiro + '/' + romaneio);
    },

    valorTotalDoRomaneio: function(romaneio) {
      if (romaneio.entregas.length > 0) return romaneio.entregas.Sum("valor");
      else return 0;
    },

    buscarPedidoComplementares: function(pedido){
      return $http.get('/api/pedidos-complementares/' + pedido);
    },

    progressoRomaneio: function(romaneio) {
      var progresso = 0;
      var total = 5;

      if (romaneio.motorista) {
        if (typeof(romaneio.motorista) == 'object') {
          if (romaneio.motorista.nome.length > 0) {
            progresso++;
          }
          if (romaneio.motorista.rg.length > 0) {
            progresso++;
          }
        } else if (romaneio.motorista != "") {
          progresso++;
        }
      }

      if (romaneio.data != null && romaneio.data != "" && typeof(romaneio.data) != 'undefined') {
        progresso++;
      }

      if (romaneio.placa != null && romaneio.placa != "" && typeof(romaneio.placa) != 'undefined') {
        progresso++;
      }

      if (romaneio.entregas.length > 0) {
        progresso++;
      }

      return progresso;
    },

    maximoProgressoRomaneio: function(romaneio) {
      return 5;
    },

    percentagemProgressoRomaneio: function(progresso, maximoProgresso) {
      return progresso / maximoProgresso * 100;
    },

    listarEntregasConfirmadas: function(carreteiro) {
      var entregasConfirmadas = [];

      if (carreteiro) {
        if (carreteiro.romaneios) {
          carreteiro.romaneios.forEach(function(romaneio) {
              romaneio.entregas.forEach(function(entrega){
                  if (entrega.pedido_agregado == 1) {
                    if (entrega.pedido_agregado_entregas_restantes == 0){
                      entrega.indice = 0;
                      entregasConfirmadas.push(entrega);
                    }
                  } else {
                    if (entrega.entregue == 1) {
                      entrega.indice = -1;
                      entregasConfirmadas.push(entrega);
                    }
                  }
              });
          });
        }
      }
      return entregasConfirmadas;
    },

    statusEntregaEntregue : function(entregue){

      var htmlOk = '<span title="Entregue"><i class="fa fa-check-square-o ok"></span>';
      var htmlErr ='<span title="Pendente (Não retornou com o canhoto ainda)"><i class="fa fa-minus-square erro"></span>';

      return $sce.trustAsHtml(entregue ? htmlOk : htmlErr);
    },

    statusEntrega : function(status){
      var htmlOk = '<span title="Ok (Era pra ser entregue)"><i class="fa fa-check-square-o ok"></i></span>';
      var htmlErr = '<span title="Erro (Não era pra ser entregue)"><i class="fa fa-minus-square erro"></span>';

      return $sce.trustAsHtml(status ? htmlOk : htmlErr);
    },

    tipoEntrega: function (tipoEntrega) {
      var resposta;
      var semResposta = "<i class='fa fa-question-circle'></i> N/A";
      var respostaColeta = "<i class='fa fa-arrow-left erro'></i> Coleta";
      var respostaEntrega = "<i class='fa fa-arrow-right ok'></i> Entrega";
      var respotaRetiraLoja = "<i class='fa fa-exclamation-triangle warn'></i> Retira Loja";
      if (tipoEntrega) {
        tipoEntrega = tipoEntrega.toUpperCase();
        resposta = tipoEntrega.toUpperCase() == 'E' ? respostaEntrega : (tipoEntrega.toUpperCase() == 'C' ? respostaColeta : (tipoEntrega.toUpperCase() == 'R' ? respotaRetiraLoja : semResposta));
      }
      else {
        resposta = semResposta;
      }
      return $sce.trustAsHtml(resposta);
    },

    buscaRomaneioAba : function(nrRomaneio, filial){
      return $http.get('/api/aba/buscaromaneio/'+ nrRomaneio +'/' + filial);
    },

    buscarTransportadora: function(param){

      return $http.get('/api/carreteiro/transportadora/' + param, {
                  params: {
                    address: param,
                    sensor: false
                  }
        }).then(function(response){

           if(response.data.statusCodeAPIGEE){
             return [];
           } else {
             return response.data.records;
           }
        });
    },

    listarEntregasFechadas: function(carreteiro, idFechamento) {
      var entregasFechadas = [];

      if (carreteiro) {
        if (carreteiro.romaneios) {
          carreteiro.romaneios.forEach(function(romaneio) {
            romaneio.entregas.forEach(function(entrega){
              if ((entrega.entregue == 2) && (idFechamento == entrega.fechamento_id)) {
                entregasFechadas.push(entrega);
              }
            });
          });
        }
      }
      return entregasFechadas;
    },

    listarAbasFechadas: function(carreteiro, idFechamento) {
      var abasFechadas = [];

      if (carreteiro) {
        if (carreteiro.abas) {
          carreteiro.abas.forEach(function(aba) {
            aba.romaneiosGemco.forEach(function(romaneio){
              if ((romaneio.status == 1) && (idFechamento == romaneio.fechamento_id)) {
                abasFechadas.push(aba);
              }
            });
          });
        }
      }
      return abasFechadas;
    },

    listarAbasConfirmados: function(carreteiro) {
      var abasConfirmados = [];

      if (carreteiro) {
        if (carreteiro.abas) {
          carreteiro.abas.forEach(function(aba) {

            aba.romaneiosGemco.forEach(function(romaneio){
              if (romaneio.status == 0) {
                abasConfirmados.push({ romaneio : romaneio.romaneio, preco : aba.preco, data: aba.data, romaneiosGemco : aba.romaneiosGemco });
              }
            });
          });
        }
      }
      return abasConfirmados;
    },
  };

}]);
