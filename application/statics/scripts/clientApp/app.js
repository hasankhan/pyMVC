define([    "jquery",
            "router",
            "logger"
            ],
        function(
            $,
            router,
            logger) {
            
    var app = {
        __listenToRequireJsErrors: function() {
            requirejs.onError = function(err) {
                logger.debug(err.requireType);
                if    (err.requireType === 'timeout')    {
                    Logger.debug('modules: ' + err);
                }
                throw    err;
            };
        },
        
        __hookUpNavigationLinks: function() {
            $("#app").on("click", "a.link", function() {
                router.navigate($(this).attr('href'), {trigger: true});
                return false;
            });
        },
    
        initialize: function() {
            router.initialize(); 

            this.__listenToRequireJsErrors()
            this.__hookUpNavigationLinks()
            
            logger.debug('initialized');        
        }
    };            

    return  app;
});
