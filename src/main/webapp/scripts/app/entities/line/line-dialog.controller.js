'use strict';

angular.module('omsApp').controller('LineDialogController',
    ['$scope', '$stateParams', '$modalInstance', 'entity', 'Line', 'Note',
        function($scope, $stateParams, $modalInstance, entity, Line, Note) {

        $scope.line = entity;
        $scope.notes = Note.query();
        $scope.load = function(id) {
            Line.get({id : id}, function(result) {
                $scope.line = result;
            });
        };

        var onSaveSuccess = function (result) {
            $scope.$emit('omsApp:lineUpdate', result);
            $modalInstance.close(result);
            $scope.isSaving = false;
        };

        var onSaveError = function (result) {
            $scope.isSaving = false;
        };

        $scope.save = function () {
            $scope.isSaving = true;
            if ($scope.line.id != null) {
                Line.update($scope.line, onSaveSuccess, onSaveError);
            } else {
                Line.save($scope.line, onSaveSuccess, onSaveError);
            }
        };

        $scope.clear = function() {
            $modalInstance.dismiss('cancel');
        };
}]);
