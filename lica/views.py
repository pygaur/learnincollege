from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext


class Dashboard(TemplateView):
    def get(self,request):
        return render_to_response("lica/dashboard.html",locals(),context_instance=RequestContext(request))
        
    def post(self,request):
        return render_to_response("lica/dashboard.html",locals(),context_instance=RequestContext(request))
        