//$(document).ready(function(){
//    $('[data-toggle="tooltip"]').tooltip();
//});

angular.module('Config', []) 
.constant('config', { 
	"linkapi": "http://127.0.0.1:8080",
	// "linkapi": "http://200.98.174.103:8080",
  "linksite": "http://127.0.0.1/contabil/",
//  "linksite": "http://200.98.174.103/contabil/",
	"versao": "v.1.2"
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
