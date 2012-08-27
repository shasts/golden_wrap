from golden_app.models import Product
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	product_list = Product.objects.all()
	return render_to_response('products.html', {'product_list' : product_list},context_instance=RequestContext(request))

def contact(request):
	return render_to_response('contact.html', context_instance=RequestContext(request))

def about(request):
	return render_to_response('contact.html', context_instance=RequestContext(request))


