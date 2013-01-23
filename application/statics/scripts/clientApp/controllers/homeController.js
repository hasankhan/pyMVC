define([    'jquery',
            'controller',
            'constants',
            'logger'],
        function(
            $,
            Controller,
            Constants,
            logger) {

    var HomeController = Controller.extend({
        
        index: function() {
            var self = this;
            
            $.getJSON('/user', function(user) {
                self._renderView('views/home.tpl.js', user);    
            });            
        },
        
        about: function(name) {
            this._renderView('views/about.tpl.js', {name: name, minAge: Constants.MIN_AGE});
        }              
    });

    return HomeController;
});
