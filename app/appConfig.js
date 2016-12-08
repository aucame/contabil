//$(document).ready(function(){
//    $('[data-toggle="tooltip"]').tooltip();
//});

angular.module('Config', []) 
.constant('config', { 
	"link": "http://127.0.0.1:8080",
//	"link": "http://200.98.174.103:8080",
	"versao": "v.1.2",
  "local": "http://127.0.0.1/contabil/"
//  "local": "http://200.98.174.103/contabil/"
})
.directive('htmlversao', function() {
  return {
    templateUrl: 'versao.html'
  };
})
.directive('htmlmenu', function() {
  return {
    templateUrl: 'menu.html'
  };
});
