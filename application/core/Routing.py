
def add_route(app, routeName, pattern, controller, action, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(routeName, action), **kwargs)