class API:
    def __init__(self, static_dir="assets"):
        self.routes = routes.routes
        self.whitenoise = Whitenoise(self.wsgi_app, root=static_dir)

    def wsgi_app(self, environ, start_response):
        request = request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)