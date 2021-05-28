from django.http import HttpResponse, response
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        return HttpResponse('<h1>Application Under Maintenance....Please try after sometime!!!!</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        e1='<h1>We are facing some technical issue. Plz try after sometime</h1><hr>'
        e2='<h2>Raised Exception: {} </h2>'.format(exception.__class__.__name__)
        e3='<h2>Exception Description/Message:{}</h2>'.format(exception)
        return HttpResponse(e1+e2+e3)