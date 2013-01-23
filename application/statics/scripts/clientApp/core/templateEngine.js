define([    "views/load",
            "hogan",
            "config"],
        function(
            templates,
            Hogan,
            Config) {

    var render = function render(name, context, partials, indent) {

        var template = false;

        if (Config.environment == "development") {
            template = require('text!' + name);
            template = Hogan.compile(template);
        } else {
            template = require(name);
        }

        return template.render(context, partials, indent);
    };

    /**
     * Gets a template
     * @param name name of the template
     * @param callback Function to call once the template is received, will add the result as a parameter
     */
    var getTemplate = function(name, callback){
        var template = false;
        if(!callback) {
            callback = function(){};
        }
        if(Config.environment == "development"){
            template = require(['text!'+name], function(result){callback(result);});
        } else {
            template = require([name], function(result){
            callback(result.render());
            });
        }
        return template;
    }

    return {
        render:render,
        getTemplate:getTemplate
    };
});
