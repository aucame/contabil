function Carreteiro() {
  this._id;
  this.nome;
  this.cnpj;
  this.filial;
  this.precos = [];
  this.motoristas = [];
  this.placas = [];
  this.abas = [];

  this.valido = function () {
    return (
      this.nome.length > 0 &&
      this.filial > 0 &&
      this.precos.fixo > 0
    );
  };

  this.CarreteiroFromSchema = function(objSchema) {
    this._id = objSchema._id;
    this.nome = objSchema.nome;
    this.filial = objSchema.filial;
    this.romaneios = objSchema.romaneios;
    this.motoristas = objSchema.motoristas;
    this.placas = objSchema.placas;
    this.cnpj = objSchema.cnpj;
    this.abas = objSchema.abas;
  };
}
