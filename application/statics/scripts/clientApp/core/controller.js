define([    'backbone',
            'templateEngine',
            'views/load',
            'logger'],
        function(
            Backbone,
            TemplateEngine,
            load,
            logger) {

    var Controller = Backbone.View.extend({
        action: null,
        args: [],
        
        initialize: function(options) {
            this.action = this[options.actionName] || function(){ };
            this.args = options.args || [];
            this.__dispatch();
        },

        _view: function(path, args) {
            return TemplateEngine.render(path, args);
        },    
        
        _renderView: function(path, args) {
            view = this._view(path, args);
            this._render(view);
        },

        _render: function(view){
            if (!view)
                return;
                
            $(this.el).html(view);
        },
        
        __dispatch: function(){
            this.action.apply(this, this.args);            
        }        
    });

    return Controller;
});
