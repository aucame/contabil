$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

angular.module('Config', [])
.constant('config', { 
	"link": "http://127.0.0.1:8080",
	"versao": "v.1.1"
});
