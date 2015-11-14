'use strict';

angular.module('omsApp')
    .factory('SimpleGsmShade', function ($resource, DateUtils) {
        return $resource('api/simpleGsmShades/:id', {}, {
            'query': { method: 'GET', isArray: true},
            'get': {
                method: 'GET',
                transformResponse: function (data) {
                    data = angular.fromJson(data);
                    return data;
                }
            },
            'update': { method:'PUT' }
        });
    });
