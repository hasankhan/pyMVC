from core.Routing import add_route

def register_routes(app):
    from controllers.HomeController import HomeController
    add_route(app, 'index', '/', HomeController, 'index')
    add_route(app, 'client_home', '/clientApp/', HomeController, 'client')
    add_route(app, 'client_page', '/clientApp/<action>', HomeController, 'client')
    
    from controllers.AccountController import AccountController
    add_route(app, 'about', '/about', AccountController, 'about', methods=['POST'])
    add_route(app, 'register', '/register', AccountController, 'register', methods=['GET'])
    add_route(app, 'register_post', '/register', AccountController, 'register_post', methods=['POST'])
    add_route(app, 'check_username', '/check', AccountController, 'user_exists', methods=['GET'])

    from controllers.AuthController import AuthController
    add_route(app, 'login', '/login', AuthController, 'login', methods=['GET'])
    add_route(app, 'login_post', '/login', AuthController, 'login_post', methods=['POST'])
    add_route(app, 'logout', '/logout', AuthController, 'logout', methods=['GET'])
    add_route(app, 'user', '/user', AuthController, 'user', methods=['GET'])
