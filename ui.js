'use strict';
(function() {

var service = angular.module('sca-product-nifti', [ ]);
service.directive('scaProductNifti', ['appconf', 'serverconf', 'toaster', 'Upload', 'resources',
function(appconf, serverconf, toaster, Upload, resources) {
    console.log("product/nifti ui.js");
}]);

//end of IIFE (immediately-invoked function expression)
})();

