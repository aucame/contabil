$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});

angular.module('Config', [])
.constant('config', { 
	"link": "http://127.0.0.1:8080",
//	"link": "http://200.98.174.103:8080",
	"versao": "v.1.1"
});

//.directive('ngLength', function NgLength() {
//		return {
//            restrict: 'A',
//            link: function($scope, $element, $attrs){
//				    $scope.$watch($attrs.ngModel, function(value) {
//					//var isValid = (value.length === 2);
//                    //ngModel.$setValidity($attrs.ngModel, isValid);
//					//alert("rwrw");
//                });				
//            }
//        };
//});
