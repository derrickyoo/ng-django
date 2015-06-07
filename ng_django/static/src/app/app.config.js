(function(){
    'use strict';

    angular
        .module('ngDjango')
        .config(configure);

    configure.$inject = ['$resourceProvider', '$urlRouterProvider', '$stateProvider'];

    function configure($resourceProvider, $urlRouterProvider, $stateProvider) {
        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;

        // Configure routing.
        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state('index', {
                url: '/'
            });
    }
}());