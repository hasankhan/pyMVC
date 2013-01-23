require.config({
    baseUrl:    window.requireJsBaseUrl,
    paths:{
        "app": "app",
        "jquery": "../libs/jquery-min",
        "backbone": "../libs/backbone-min",
        "hogan"    : "../libs/hogan-min",
        "underscore": "../libs/underscore-min",
        "logger": "../libs/JSLog-min",
        "config": "config/" + window.jsConfig,
        "router": "router",
        "templateEngine" : "core/templateEngine",
        "controller" : "core/controller"
    },
    
    shim: {
        'backbone': {
            //These script dependencies should be loaded before loading backbone.js
            deps: ['underscore', 'jquery'],
            //Once loaded, use the global 'Backbone' as the
            //module value.
            exports: 'Backbone'
        }
    },

    "package": [{name:"templates", location:"Views"}],

    waitSeconds:    30
});

require(['app'], function(app) {
    app.initialize();
});
