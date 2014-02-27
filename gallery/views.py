from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Image

def homepage(request):
    
    template = loader.get_template('index.html')
    images = Image.objects.all()
    context = RequestContext(request, {
        'images': images
    })
    return HttpResponse(template.render(context))
    
