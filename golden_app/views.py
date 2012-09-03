from golden_app.models import Product,CartManager
from django.shortcuts import render_to_response,get_object_or_404 
from django.template import RequestContext

def index(request):
	product_list = Product.objects.all()
	return render_to_response('products.html', {'product_list' : product_list},context_instance=RequestContext(request))

def contact(request):
	return render_to_response('contact.html', context_instance=RequestContext(request))

def about(request):
	return render_to_response('contact.html', context_instance=RequestContext(request))

def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render_to_response('detail.html', {'product' : product}, context_instance=RequestContext(request))

def add_to_cart(request):
	CartManager.add_to_cart(request,product_id,quantity)


