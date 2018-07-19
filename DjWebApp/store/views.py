from django.shortcuts import render, redirect
from store.forms import ProductApplyForm
from django.template import RequestContext
from store.models import UserProduct
from django.http import HttpResponse
from django.template import loader
from django.http import Http404


def index(request):
    all_products = UserProduct.objects.all()
    #template = loader.get_template('store/index.html')
    context = {
        'all_products': all_products, 
        }
    return render(request,'store/index.html', context)
  #  html = ''
  #  for product in all_products:
  #      url = '/item/' + str(product.id) + '/'
  #      html += '<a href="' + url + '">' + product.productName + '</a><br>'
  #  return HttpResponse(html)
  #  return HttpResponse(template.render(context, request))



def add(request):
    if request.method =='POST':
        SGForm = ProductApplyForm(request.POST, request.FILES)
        if SGForm.is_valid():
            data = SGForm.cleaned_data
            Product = UserProduct()
            Product.userId = data['userId']
            Product.productName = data['productName']
            Product.description = data['description']
            Product.price = data['price']
            Product.Category = data['category']
            Product.image = request.FILES['image']#data['image']
            Product.save()

            return redirect ('/add')
    else:
        SGForm = ProductApplyForm()
    context ={'SGForm': SGForm}
    return render(request,'store/addproduct.html', context)#, RequestContext(request) )

def item(request, prod_id):
    try:
        product1 = UserProduct.objects.get(pk=prod_id)
    except UserProduct.DoesNotExist:
        raise Http404("Товар не существует")
    contextItem ={'product1': product1, 'prod_id':prod_id}
    return render(request,'store/item.html', contextItem)
   # return HttpResponse("<h2>Здесть можно увидеть детали интересующих товарров</h2>" + str(prod_id))
