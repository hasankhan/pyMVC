define([    'jquery',
            'backbone',
            'controllers/homeController',
            'logger'],
        function(
            $,
            Backbone,
            HomeController,
            logger) {

    var AppRouter = Backbone.Router.extend({

        initialize: function() {
            //Fix for facebook bug
            if (window.location.hash == '#_=_') {
                window.location.hash = '';
            }
        },

        // Routing
        routes: {
            ":action": "homeAction",
            ":action/:id": "homeAction",
            "*actions": "defaultAction" // default route
        },        
        
        defaultAction: function(actions) {
            this.homeAction('index');
        },

        homeAction: function() {
            args = Array.prototype.slice.call(arguments) // turn args object into array
            actionName = args.shift()
            var self = this;
            
            $(document).ready(function () {
                var el = $('#app');
                var home = new HomeController({
                    el: el, 
                    actionName: actionName, 
                    args: args}
                );
            });
        }
    });

    var router = new AppRouter();
    Backbone.history.start({
        pushState: true,
        root: "/clientApp/"
    });

    return router;
});
