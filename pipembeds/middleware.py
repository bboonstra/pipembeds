from django.utils.deprecation import MiddlewareMixin

class CSPMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "frame-ancestors *"
        return response
