from golden_app.models import Product
from django.shortcuts import render_to_response

def index(request):
	product_list = Product.objects.all()
	return render_to_response('products/index.html', {'product_list' : product_list})
